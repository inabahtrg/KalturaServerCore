
CREATE TABLE `batch_job_log`
(
    `id` INTEGER  NOT NULL AUTO_INCREMENT,
    `job_id` INTEGER,
    `job_type` SMALLINT,
    `job_sub_type` SMALLINT,
    `data` TEXT,
    `file_size` INTEGER,
    `duplication_key` VARCHAR(2047),
    `status` INTEGER,
    `log_status` INTEGER,
    `abort` TINYINT,
    `check_again_timeout` INTEGER,
    `progress` TINYINT,
    `message` VARCHAR(1024),
    `description` VARCHAR(1024),
    `updates_count` SMALLINT,
    `created_at` DATETIME,
    `created_by` VARCHAR(20),
    `updated_at` DATETIME,
    `updated_by` VARCHAR(20),
    `deleted_at` DATETIME,
    `priority` TINYINT,
    `work_group_id` INTEGER,
    `queue_time` DATETIME,
    `finish_time` DATETIME,
    `entry_id` VARCHAR(20) default '',
    `partner_id` INTEGER default 0,
    `subp_id` INTEGER default 0,
    `scheduler_id` INTEGER,
    `worker_id` INTEGER,
    `batch_index` INTEGER,
    `last_scheduler_id` INTEGER,
    `last_worker_id` INTEGER,
    `last_worker_remote` TINYINT,
    `processor_expiration` DATETIME,
    `execution_attempts` TINYINT,
    `lock_version` INTEGER,
    `twin_job_id` INTEGER,
    `bulk_job_id` INTEGER,
    `root_job_id` INTEGER,
    `parent_job_id` INTEGER,
    `dc` INTEGER,
    `err_type` INTEGER,
    `err_number` INTEGER,
    `on_stress_divert_to` INTEGER,
    `param_1` INTEGER,
    `param_2` VARCHAR(255),
    `param_3` VARCHAR(255),
    `param_4` INTEGER,
    `param_5` VARCHAR(255),
    `log_status` INTEGER,
	`job_id` INTEGER,
    PRIMARY KEY (`id`),
    KEY `status_job_type_index`(`partner_id`, `status`, `job_type`),
    KEY `job_id_index`(`job_id`),
    KEY `partner_id_index`(`partner_id`)
)Type=InnoDB;
