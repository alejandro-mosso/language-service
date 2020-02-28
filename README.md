#Environment set up
<ul>
    <li>If Docker service is not started, run below commands:
        <br/><code><b>$</b> sudo service docker start</code>
        <br/><code><b>$</b> sudo service docker status</code>
    </li>
    <li>Run following commands under language-services:
        <br/><code><b>$</b> docker-compose build</code>
        <br/><code><b>$</b> docker-compose up</code>
    </li>
</ul>

#Django project creation
<ul>
    <li>Under language-service directory run:
    <br/><code><b>$</b> django-admin startproject app</code>
    <br/><code><b>$</b> cd app</code>
    <br/><code><b>$</b> python3 manage.py startapp translate</code>
    <br/><code><b>$</b> python3 manage.py startapp define</code>
    <br/><code><b>$</b> python3 manage.py startapp youglish</code>
    <br/><code><b>$</b> python3 manage.py startapp audio</code>
    </li>
</ul>