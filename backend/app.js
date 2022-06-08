'use strict'
require('dotenv').config();

const path = require('path');
const AutoLoad = require('@fastify/autoload');

module.exports = async function (fastify, opts) {
  fastify.register(require('@fastify/cors'), { 
    origin: true
  })



  fastify.register(require('@fastify/mysql'), {
    host: process.env.DB_HOST,
    user: process.env.DB_USERNAME,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE
  })

  // Do not touch the following lines

  // This loads all plugins defined in plugins
  // those should be support plugins that are reused
  // through your application
  fastify.register(AutoLoad, {
    dir: path.join(__dirname, 'plugins'),
    options: Object.assign({}, opts)
  })

  // This loads all plugins defined in routes
  // define your routes in one of these
  fastify.register(AutoLoad, {
    dir: path.join(__dirname, 'routes'),
    options: Object.assign({}, opts)
  })
}
