<title>table generator</title>

<form>
    <label>cols: <input type="number" name="cols"></label>
    <label>rows: <input type="number" name="rows"></label>

    <select name="cont">
        <option value="noval">brak wartości</option>
        <option value="multable">tabliczka mnożenia</option>
        <option value="userval">podaj wartość</option>
        <option value="randval">losowa liczba</option>
    </select>

    <div id="userval" class="hide">
        <label>podaj wartość: <input type="text" name="userval"></label>
    </div>

    <div id="randval" class="hide">
        <label>min: <input type="number" name="min"></label>
        <label>max: <input type="number" name="max"></label>
    </div>

    <input type="submit" value="generate">
</form>

<?php if (isset($_GET['cols']) && isset($_GET['rows'])): ?>
    <table>
    <?php for ($y = 0; $y < +$_GET['cols']; $y++): ?>
        <tr>
        <?php for ($x = 0; $x < +$_GET['rows']; $x++): ?>
            <td>
                <?php
                    if ($_GET['cont'] == 'multable'):
                        echo ($x + 1) * ($y + 1);
                    elseif ($_GET['cont'] == 'userval'):
                        echo $_GET['userval'];
                    elseif ($_GET['cont'] == 'randval'):
                        if (!empty($_GET['min']) && !empty($_GET['max'])):
                            echo rand(+$_GET['min'], +$_GET['max']);
                        endif;
                    endif;
                ?>
            </td>
        <?php endfor; ?>
        </tr>
    <?php endfor; ?>
    </table>
<?php endif; ?>

<style>
    td {
        padding: 10px;
        border: 1px solid black;
        text-align: center;
        transition: 2s;

        &:hover {
            background-color: red;
            transition: 0s;
        }
    }

    .hide {
        display: none;
    }

    .show {
        display: block !important;
    }
</style>

<script>
    const $ = (sel, ctx = document.body) => ctx.querySelector(sel)
    const $$ = (sel, ctx = document.body) => [...ctx.querySelectorAll(sel)]

    $('select').onchange = () => {
        $$('.show').forEach(n => n.classList.remove('show'))

        const n = $(`#${$('select').value}`)
        if (n) n.classList.add('show')
    }
</script>