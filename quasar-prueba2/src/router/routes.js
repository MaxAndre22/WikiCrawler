const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: '', component: () => import('pages/HomePage.vue') },
      { path: 'word/:keyword', name: 'word', prop: true, component: () => import('pages/WordPage.vue') },
      { path: 'wiki/:keyword', name: 'wiki', prop: true, component: () => import('pages/WikipediaPage.vue') }
  ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
