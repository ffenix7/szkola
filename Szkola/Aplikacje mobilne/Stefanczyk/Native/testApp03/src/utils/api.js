import {
  getNotes,
  getServerBaseUrl,
  normalizeNotes,
  saveNotes,
} from './storage';

const requestJson = async (path, options = {}) => {
  const baseUrl = await getServerBaseUrl();
  const response = await fetch(`${baseUrl}${path}`, {
    ...options,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      ...(options.headers ?? {}),
    },
  });

  const text = await response.text();
  const data = text ? JSON.parse(text) : null;

  if (!response.ok) {
    throw new Error(
      data?.message ??
        `Serwer zwrócił status ${response.status}.`
    );
  }

  return data;
};

export const backupNotesToServer = async () => {
  const notes = await getNotes();

  return requestJson('/api/task/backup', {
    method: 'POST',
    body: JSON.stringify({ notes }),
  });
};

export const restoreNotesFromServer = async () => {
  const data = await requestJson('/api/task');
  const notes = normalizeNotes(data);

  await saveNotes(notes);

  return notes;
};

export const clearServerNotes = async () =>
  requestJson('/api/task', {
    method: 'DELETE',
  });
