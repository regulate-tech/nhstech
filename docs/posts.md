---
layout: default
title: news
permalink: /posts/
---

# Project News

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
      <h2>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h2>
      <p>
        {{ post.excerpt | strip_html | truncate: 150 }}
      </p>
    </li>
  {% endfor %}
</ul>