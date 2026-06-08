import * as SecureStore from 'expo-secure-store';

export const NOTES_KEY = 'notes';
export const CATEGORIES_KEY = 'categories';
export const SERVER_IP_KEY = 'server_ip';
export const SERVER_PORT_KEY = 'server_port';

export const DEFAULT_CATEGORY = {
  id: 'default',
  name: 'Ogólne',
};

export const DEFAULT_SERVER_CONFIG = {
  ip: '127.0.0.1',
  port: '3000',
};

const safeParse = (value, fallback) => {
  try {
    return value ? JSON.parse(value) : fallback;
  } catch (error) {
    console.log('Błąd parsowania danych:', error);
    return fallback;
  }
};

export const normalizeCategories = (items) => {
  const source = Array.isArray(items) ? items : [];
  const categories = source
    .map((item, index) => {
      if (typeof item === 'string') {
        return {
          id: item || index,
          name: item.trim(),
        };
      }

      return {
        id: item?.id ?? item?.name ?? index,
        name: String(item?.name ?? '').trim(),
      };
    })
    .filter((item) => item.name.length > 0);

  const hasDefault = categories.some(
    (item) =>
      item.name.toLowerCase() ===
      DEFAULT_CATEGORY.name.toLowerCase()
  );

  return hasDefault
    ? categories
    : [DEFAULT_CATEGORY, ...categories];
};

export const normalizeNotes = (items) => {
  const source = Array.isArray(items) ? items : [];

  return source.map((note, index) => ({
    id:
      note?.id ??
      note?._id ??
      `${Date.now()}-${index}`,
    title: String(note?.title ?? '').trim(),
    desc: String(note?.desc ?? '').trim(),
    category:
      String(note?.category ?? '').trim() ||
      DEFAULT_CATEGORY.name,
    createdAt:
      note?.createdAt ?? new Date().toISOString(),
  }));
};

export const getCategories = async () => {
  const storedCategories = await SecureStore.getItemAsync(
    CATEGORIES_KEY
  );

  return normalizeCategories(
    safeParse(storedCategories, [])
  );
};

export const saveCategories = async (categories) => {
  await SecureStore.setItemAsync(
    CATEGORIES_KEY,
    JSON.stringify(normalizeCategories(categories))
  );
};

export const addCategory = async (name) => {
  const cleanName = name.trim();
  const categories = await getCategories();
  const exists = categories.some(
    (item) =>
      item.name.toLowerCase() ===
      cleanName.toLowerCase()
  );

  if (exists) {
    return {
      added: false,
      categories,
    };
  }

  const updatedCategories = [
    ...categories,
    {
      id: Date.now(),
      name: cleanName,
    },
  ];

  await saveCategories(updatedCategories);

  return {
    added: true,
    categories: updatedCategories,
  };
};

export const getNotes = async () => {
  const storedNotes = await SecureStore.getItemAsync(
    NOTES_KEY
  );

  return normalizeNotes(safeParse(storedNotes, []));
};

export const saveNotes = async (notes) => {
  await SecureStore.setItemAsync(
    NOTES_KEY,
    JSON.stringify(normalizeNotes(notes))
  );
};

export const clearNotes = async () => {
  await SecureStore.setItemAsync(
    NOTES_KEY,
    JSON.stringify([])
  );
};

export const getServerConfig = async () => {
  const ip =
    (await SecureStore.getItemAsync(SERVER_IP_KEY)) ??
    DEFAULT_SERVER_CONFIG.ip;

  const port =
    (await SecureStore.getItemAsync(SERVER_PORT_KEY)) ??
    DEFAULT_SERVER_CONFIG.port;

  return {
    ip,
    port,
  };
};

export const saveServerConfig = async ({ ip, port }) => {
  await SecureStore.setItemAsync(SERVER_IP_KEY, ip.trim());
  await SecureStore.setItemAsync(
    SERVER_PORT_KEY,
    port.trim()
  );
};

export const getServerBaseUrl = async () => {
  const { ip, port } = await getServerConfig();
  const cleanIp = ip.trim();
  const cleanPort = port.trim();

  if (!cleanIp || !cleanPort) {
    throw new Error('Ustaw adres IP i port serwera.');
  }

  return `http://${cleanIp}:${cleanPort}`;
};
