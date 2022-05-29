const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "home", component: () => import("pages/HomePage.vue") },
      { path: "index", component: () => import("pages/IndexPage.vue") },
      {
        path: "word/:keyword",
        name: "word",
        prop: true,
        component: () => import("pages/WordPage.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
