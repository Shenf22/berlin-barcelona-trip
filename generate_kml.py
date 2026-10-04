import json

with open('verified_images.json', 'r', encoding='utf-8') as f:
    images = json.load(f)

kml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Берлин - Барселона: Все точки и смотровые площадки</name>
    <description>Интерактивная карта переезда: фото, координаты и приоритеты.</description>
    
    <Style id="tier1">
      <IconStyle>
        <scale>1.3</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/red-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="tier2">
      <IconStyle>
        <scale>1.1</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/blue-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="tier3">
      <IconStyle>
        <scale>1.0</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/yellow-dot.png</href></Icon>
      </IconStyle>
    </Style>
    <Style id="finish">
      <IconStyle>
        <scale>1.4</scale>
        <Icon><href>http://maps.google.com/mapfiles/ms/icons/green-dot.png</href></Icon>
      </IconStyle>
    </Style>

    <Folder>
      <name>🔥 Tier 1: Высший приоритет (Мастхэв)</name>
      
      <Placemark>
        <name>★ Шамони и пик Монблан (4808 м)</name>
        <description><![CDATA[
          <h3>Шамони-Монблан</h3>
          <p><b>Высшая точка Европы (4 808 м).</b> Гигантские ледники, отвесные скалы.</p>
          <img src="{images['Mont Blanc']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier1</styleUrl>
        <Point><coordinates>6.8694,45.9237,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Виадук Мийо (Мост выше Эйфелевой башни)</name>
        <description><![CDATA[
          <h3>Виадук Мийо</h3>
          <p><b>Самый высокий вантовый мост в мире (опора 343 м).</b> Езда буквально над облаками через каньон Тарн.</p>
          <img src="{images['Millau Viaduct']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier1</styleUrl>
        <Point><coordinates>3.0219,44.0772,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Крепость Каркассон</name>
        <description><![CDATA[
          <h3>Cité de Carcassonne</h3>
          <p><b>Крупнейшая крепость Европы.</b> 3 км двойных каменных стен, 52 башни, ров. Вечером грандиозная подсветка.</p>
          <img src="{images['Cité de Carcassonne']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier1</styleUrl>
        <Point><coordinates>2.3636,43.2064,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Римский акведук Пон-дю-Гар</name>
        <description><![CDATA[
          <h3>Пон-дю-Гар (I век н.э.)</h3>
          <p><b>49-метровый каменный мост-великан</b> над рекой Гардон. Построен римлянами без раствора.</p>
          <img src="{images['Pont du Gard']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier1</styleUrl>
        <Point><coordinates>4.5350,43.9475,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>★ Шильонский замок (Женевское озеро)</name>
        <description><![CDATA[
          <h3>Château de Chillon</h3>
          <p><b>Каменный замок прямо на воде</b> Женевского озера на фоне заснеженных альпийских хребтов.</p>
          <img src="{images['Château de Chillon']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier1</styleUrl>
        <Point><coordinates>6.9275,46.4142,0</coordinates></Point>
      </Placemark>
    </Folder>

    <Folder>
      <name>✨ Tier 2: Высокий приоритет (Очень зрелищно)</name>
      
      <Placemark>
        <name>Ущелье Лаутербруннен (Швейцария)</name>
        <description><![CDATA[
          <h3>Долина 72 водопадов</h3>
          <p>Отвесные километровые скалы, вокруг пики Эйгер, Мёнх и Юнгфрау. Прообраз Ривенделла из Властелина Колец.</p>
          <img src="{images['Lauterbrunnen']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier2</styleUrl>
        <Point><coordinates>7.9077,46.5935,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Рейнский водопад (Rheinfall)</name>
        <description><![CDATA[
          <h3>Самый мощный водопад Европы</h3>
          <p>Стена ревущей воды шириной 150 метров прямо на границе Германии и Швейцарии.</p>
          <img src="{images['Rhine Falls']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier2</styleUrl>
        <Point><coordinates>8.6156,47.6778,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Коллиур (Средиземное море и Пиренеи)</name>
        <description><![CDATA[
          <h3>Королевский замок на берегу моря</h3>
          <p>Точка, где горы уходят в море. Скалы, волны, первый морской воздух.</p>
          <img src="{images['Collioure']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier2</styleUrl>
        <Point><coordinates>3.0817,42.5250,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Жирона (Крепостная стена Passeig de la Muralla)</name>
        <description><![CDATA[
          <h3>Крепостной гребень над городом</h3>
          <p>Пеший проход по высокой древней стене над крышами города с видом на горы.</p>
          <img src="{images['Girona']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier2</styleUrl>
        <Point><coordinates>2.8214,41.9794,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Тосса-де-Мар (Крепость над морем)</name>
        <description><![CDATA[
          <h3>Башни на скале Коста-Брава</h3>
          <p>Средневековая крепость прямо на утесе над бирюзовой морской бухтой.</p>
          <img src="{images['Tossa de Mar']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier2</styleUrl>
        <Point><coordinates>2.9328,41.7225,0</coordinates></Point>
      </Placemark>
    </Folder>

    <Folder>
      <name>💡 Tier 3: Бонусные точки по пути</name>
      
      <Placemark>
        <name>Театр-музей Сальвадора Дали (Фигерас)</name>
        <description><![CDATA[
          <h3>Музей Дали</h3>
          <p>Безумное здание с гигантскими яйцами на крыше прямо у скоростной трассы AP-7 при въезде в Испанию.</p>
          <img src="{images['Dalí Theatre and Museum']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier3</styleUrl>
        <Point><coordinates>2.9597,42.2680,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Крепость Кайзербург (Нюрнберг)</name>
        <description><![CDATA[
          <h3>Баварская цитадель</h3>
          <p>Каменная крепость на высокой скале над старым городом.</p>
          <img src="{images['Nuremberg Castle']['thumb']}" width="300" />
        ]]></description>
        <styleUrl>#tier3</styleUrl>
        <Point><coordinates>11.0758,49.4578,0</coordinates></Point>
      </Placemark>

      <Placemark>
        <name>Барселона (Финиш)</name>
        <description><![CDATA[
          <h3>Добро пожаловать в новый дом! 🎉</h3>
          <p>Конечная точка великого переезда.</p>
        ]]></description>
        <styleUrl>#finish</styleUrl>
        <Point><coordinates>2.1734,41.3851,0</coordinates></Point>
      </Placemark>
    </Folder>
  </Document>
</kml>
"""

with open('berlin_barcelona_route.kml', 'w', encoding='utf-8') as f:
    f.write(kml_template)

print("KML updated successfully with images and priority categories!")
