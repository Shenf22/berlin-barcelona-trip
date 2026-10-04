import json

with open('verified_images.json', 'r', encoding='utf-8') as f:
    images = json.load(f)

kml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Берлин ➔ Барселона: Маршрут по дням и точки</name>
    <description>Полноценный роудтрип: основной маршрут по дням с линией пути + топовые горные крюки.</description>
    
    <!-- Стили -->
    <Style id="dayPoint">
      <IconStyle>
        <scale>1.2</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/blue-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="detourPoint">
      <IconStyle>
        <scale>1.3</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/yellow-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="finishPoint">
      <IconStyle>
        <scale>1.4</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/green-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="mainRouteLine">
      <LineStyle>
        <color>ffd14836</color>
        <width>5</width>
      </LineStyle>
    </Style>
    <Style id="detourRouteLine">
      <LineStyle>
        <color>ff0288d1</color>
        <width>4</width>
      </LineStyle>
    </Style>

    <!-- СЛОЙ 1: ОСНОВНОЙ МАРШРУТ ПО ДНЯМ -->
    <Folder>
      <name>📅 Основной маршрут по дням (День 1 - 7)</name>
      
      <Placemark>
        <name>День 0: Берлин (Старт)</name>
        <description><![CDATA[
          <h3>Берлин (Германия)</h3>
          <p>Точка старта большого переезда.</p>
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>13.404954,52.520008,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 1: Крепость Кайзербург (Нюрнберг)</name>
        <description><![CDATA[
          <h3>День 1 • Крепость Кайзербург (Нюрнберг)</h3>
          <p><b>Перегон:</b> ~440 км (~4.5 ч).<br>
          Мощная каменная цитадель на скале над старым городом.</p>
          <img src="{images['Nuremberg Castle']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>11.075833,49.457778,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 2: Озеро Люцерн и Альпы</name>
        <description><![CDATA[
          <h3>День 2 • Озеро Люцерн и Альпы (Швейцария)</h3>
          <p><b>Перегон:</b> ~400 км (~4.5 ч).<br>
          Заснеженные двухтысячники Пилатус и Риги прямо над кристальным озером.</p>
          <img src="{images['Rhine Falls']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>8.309307,47.050168,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 3 (утро): Шильонский замок</name>
        <description><![CDATA[
          <h3>День 3 • Шильонский замок (Женевское озеро)</h3>
          <p><b>Перегон:</b> ~200 км (~2.5 ч).<br>
          Каменный средневековый замок на воде на фоне заснеженных хребтов Альп.</p>
          <img src="{images['Château de Chillon']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>6.927500,46.414167,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 3 (вечер): Анси (Франция)</name>
        <description><![CDATA[
          <h3>День 3 (вечер) • Анси (Франция)</h3>
          <p><b>Перегон:</b> ~85 км (~1 ч).<br>
          Городок на чистейшем горном озере с замком-тюрьмой посреди реки.</p>
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>6.129384,45.899247,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 4: Римский акведук Пон-дю-Гар</name>
        <description><![CDATA[
          <h3>День 4 • Акведук Пон-дю-Гар</h3>
          <p><b>Перегон:</b> ~340 км (~3.5 ч).<br>
          Каменный мост-акведук высотой 49 метров (высота 16-этажки!), построенный римлянами 2000 лет назад без раствора.</p>
          <img src="{images['Pont du Gard']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>4.535000,43.947500,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 5: Крепость Каркассон</name>
        <description><![CDATA[
          <h3>День 5 • Город-крепость Каркассон</h3>
          <p><b>Перегон:</b> ~240 км (~2.5 ч).<br>
          Самая большая крепость в Европе: 3 км двойных каменных стен, 52 башни, ров. Вечером включается ночная подсветка.</p>
          <img src="{images['Cité de Carcassonne']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>2.363611,43.206389,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 6 (день): Коллиур (Средиземное море)</name>
        <description><![CDATA[
          <h3>День 6 • Коллиур (Франция ➔ Море)</h3>
          <p><b>Перегон:</b> ~140 км (~1.5 ч).<br>
          Пиренеи упираются в море, средневековый замок на пляже, первый морской воздух.</p>
          <img src="{images['Collioure']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>3.081667,42.525000,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 6 (вечер): Жирона (Испания)</name>
        <description><![CDATA[
          <h3>День 6 (вечер) • Жирона (Испания)</h3>
          <p><b>Перегон:</b> ~95 км (~1 ч).<br>
          Проход по гребню древней крепостной стены Passeig de la Muralla над крышами старого города.</p>
          <img src="{images['Girona']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>2.821426,41.979401,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 7 (утро): Тосса-де-Мар (Коста-Брава)</name>
        <description><![CDATA[
          <h3>День 7 • Тосса-де-Мар</h3>
          <p><b>Перегон:</b> ~40 км (~45 мин).<br>
          Крепость на скале прямо над пляжем и бирюзовыми бухтами Коста-Брава.</p>
          <img src="{images['Tossa de Mar']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#dayPoint</styleUrl>
        <Point><coordinates>2.932778,41.722500,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>День 7 (финиш): Барселона 🎉</name>
        <description><![CDATA[
          <h3>День 7 (финал) • Барселона</h3>
          <p><b>Перегон:</b> ~90 км (~1.2 ч).<br>
          Финишная точка великого переезда. Новый дом!</p>
        ]]></description>
        <styleUrl>#finishPoint</styleUrl>
        <Point><coordinates>2.173403,41.385064,0</coordinates></Point>
      </Placemark>

      <!-- Нить основного маршрута -->
      <Placemark>
        <name>Линия основного маршрута (7 дней)</name>
        <styleUrl>#mainRouteLine</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <coordinates>
            13.404954,52.520008,0
            11.075833,49.457778,0
            8.309307,47.050168,0
            6.927500,46.414167,0
            6.129384,45.899247,0
            4.535000,43.947500,0
            2.363611,43.206389,0
            3.081667,42.525000,0
            2.821426,41.979401,0
            2.932778,41.722500,0
            2.173403,41.385064,0
          </coordinates>
        </LineString>
      </Placemark>
    </Folder>

    <!-- СЛОЙ 2: ТОПОВЫЕ КРЮКИ И АЛЬТЕРНАТИВЫ -->
    <Folder>
      <name>⚡ Эпические крюки (Монблан, Мост Мийо, Каньоны)</name>
      
      <Placemark>
        <name>★ Крюк Дня 3: Шамони и пик Монблан (4 808 м)</name>
        <description><![CDATA[
          <h3>Шамони-Монблан</h3>
          <p><b>Высшая точка Европы (4 808 м).</b> Гигантские ледники, отвесные скалы.<br>
          <i>Добавляет +1.5 ч к Дню 3 между Женевой и Анси.</i></p>
          <img src="{images['Mont Blanc']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#detourPoint</styleUrl>
        <Point><coordinates>6.869400,45.923700,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Крюк Дня 4-5: Виадук Мийо (Мост 343 м)</name>
        <description><![CDATA[
          <h3>Виадук Мийо (Трасса A75)</h3>
          <p><b>Самый высокий вантовый мост в мире (опора 343 м — выше Эйфелевой башни!).</b><br>
          Езда буквально над облаками через гигантский каньон Тарн.<br>
          <i>Альтернатива трассе по долине между Пон-дю-Гар и Каркассоном.</i></p>
          <img src="{images['Millau Viaduct']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#detourPoint</styleUrl>
        <Point><coordinates>3.021944,44.077222,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Крюк Дня 2: Рейнский водопад (Rheinfall)</name>
        <description><![CDATA[
          <h3>Рейнский водопад</h3>
          <p><b>Самый мощный водопад Европы</b> (150 м шириной).<br>
          <i>Находится прямо на границе Германии и Швейцарии по пути к Люцерну.</i></p>
          <img src="{images['Rhine Falls']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#detourPoint</styleUrl>
        <Point><coordinates>8.615600,47.677800,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Крюк Дня 2-3: Ущелье Лаутербруннен</name>
        <description><![CDATA[
          <h3>Долина 72 водопадов</h3>
          <p>Отвесные километровые скалы, вокруг пики Эйгер, Мёнх и Юнгфрау. Прообраз Ривенделла.<br>
          <i>Крюк +1 ч от Люцерна.</i></p>
          <img src="{images['Lauterbrunnen']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#detourPoint</styleUrl>
        <Point><coordinates>7.907700,46.593500,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Крюк Дня 6: Музей Сальвадора Дали (Фигерас)</name>
        <description><![CDATA[
          <h3>Театр-музей Дали</h3>
          <p>Сюрреалистичный замок с гигантскими яйцами прямо у трассы AP-7 при въезде в Испанию.</p>
          <img src="{images['Dalí Theatre and Museum']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#detourPoint</styleUrl>
        <Point><coordinates>2.959700,42.268000,0</coordinates></Point>
      </Placemark>
    </Folder>

  </Document>
</kml>
"""

with open('berlin_barcelona_route.kml', 'w', encoding='utf-8') as f:
    f.write(kml_template)

print("berlin_barcelona_route.kml updated with Day-by-Day sequence + visual line track + detours!")
