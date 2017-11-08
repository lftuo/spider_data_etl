-- iPhone型号表建表语句
CREATE TABLE iphone_model
(
  phone_name    VARCHAR(100) NULL,
  type          VARCHAR(100) NULL,
  Internal_Name VARCHAR(100) NULL,
  Identifier    VARCHAR(100) NULL
);

-- 爬虫结果表建表语句
CREATE TABLE shouji_all_spider_data
(
  id               VARCHAR(50)  NULL,
  title            VARCHAR(200) NULL,
  price            VARCHAR(20)  NULL,
  screen_size      TEXT         NULL,
  screen_material  VARCHAR(100) NULL,
  resolution       VARCHAR(100) NULL,
  opreating_system TEXT         NULL,
  cpu_name         VARCHAR(100) NULL,
  core_nums        VARCHAR(50)  NULL,
  ram              TEXT         NULL,
  rom              TEXT         NULL,
  phone_color      VARCHAR(100) NULL,
  phone_material   TEXT         NULL,
  sim              VARCHAR(100) NULL,
  sim_max_nums     VARCHAR(50)  NULL,
  battery          VARCHAR(50)  NULL,
  type1            TEXT         NULL,
  type2            TEXT         NULL,
  model            TEXT         NULL,
  time             VARCHAR(50)  NULL,
  url              VARCHAR(100) NULL,
  data_source      VARCHAR(100) NULL,
  brand            VARCHAR(100) NULL
);