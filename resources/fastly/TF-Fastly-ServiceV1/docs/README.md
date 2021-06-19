# TF::Fastly::ServiceV1

Provides a Fastly Service, representing the configuration for a website, app,
API, or anything else to be served through Fastly. A Service encompasses Domains
and Backends.

The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly's guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::ServiceV1",
    "Properties" : {
        "<a href="#activate" title="Activate">Activate</a>" : <i>Boolean</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#defaulthost" title="DefaultHost">DefaultHost</a>" : <i>String</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versioncomment" title="VersionComment">VersionComment</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backenddefinition.md">BackendDefinition</a>, ... ]</i>,
        "<a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>" : <i>[ <a href="bigqueryloggingdefinition.md">BigqueryloggingDefinition</a>, ... ]</i>,
        "<a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>" : <i>[ <a href="blobstorageloggingdefinition.md">BlobstorageloggingDefinition</a>, ... ]</i>,
        "<a href="#cachesetting" title="CacheSetting">CacheSetting</a>" : <i>[ <a href="cachesettingdefinition.md">CacheSettingDefinition</a>, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>,
        "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ <a href="dictionarydefinition.md">DictionaryDefinition</a>, ... ]</i>,
        "<a href="#director" title="Director">Director</a>" : <i>[ <a href="directordefinition.md">DirectorDefinition</a>, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>[ <a href="domaindefinition.md">DomainDefinition</a>, ... ]</i>,
        "<a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>" : <i>[ <a href="dynamicsnippetdefinition.md">DynamicsnippetDefinition</a>, ... ]</i>,
        "<a href="#gcslogging" title="Gcslogging">Gcslogging</a>" : <i>[ <a href="gcsloggingdefinition.md">GcsloggingDefinition</a>, ... ]</i>,
        "<a href="#gzip" title="Gzip">Gzip</a>" : <i>[ <a href="gzipdefinition.md">GzipDefinition</a>, ... ]</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthcheckDefinition</a>, ... ]</i>,
        "<a href="#httpslogging" title="Httpslogging">Httpslogging</a>" : <i>[ <a href="httpsloggingdefinition.md">HttpsloggingDefinition</a>, ... ]</i>,
        "<a href="#logentries" title="Logentries">Logentries</a>" : <i>[ <a href="logentriesdefinition.md">LogentriesDefinition</a>, ... ]</i>,
        "<a href="#loggingcloudfiles" title="LoggingCloudfiles">LoggingCloudfiles</a>" : <i>[ <a href="loggingcloudfilesdefinition.md">LoggingCloudfilesDefinition</a>, ... ]</i>,
        "<a href="#loggingdatadog" title="LoggingDatadog">LoggingDatadog</a>" : <i>[ <a href="loggingdatadogdefinition.md">LoggingDatadogDefinition</a>, ... ]</i>,
        "<a href="#loggingdigitalocean" title="LoggingDigitalocean">LoggingDigitalocean</a>" : <i>[ <a href="loggingdigitaloceandefinition.md">LoggingDigitaloceanDefinition</a>, ... ]</i>,
        "<a href="#loggingelasticsearch" title="LoggingElasticsearch">LoggingElasticsearch</a>" : <i>[ <a href="loggingelasticsearchdefinition.md">LoggingElasticsearchDefinition</a>, ... ]</i>,
        "<a href="#loggingftp" title="LoggingFtp">LoggingFtp</a>" : <i>[ <a href="loggingftpdefinition.md">LoggingFtpDefinition</a>, ... ]</i>,
        "<a href="#logginggooglepubsub" title="LoggingGooglepubsub">LoggingGooglepubsub</a>" : <i>[ <a href="logginggooglepubsubdefinition.md">LoggingGooglepubsubDefinition</a>, ... ]</i>,
        "<a href="#loggingheroku" title="LoggingHeroku">LoggingHeroku</a>" : <i>[ <a href="loggingherokudefinition.md">LoggingHerokuDefinition</a>, ... ]</i>,
        "<a href="#logginghoneycomb" title="LoggingHoneycomb">LoggingHoneycomb</a>" : <i>[ <a href="logginghoneycombdefinition.md">LoggingHoneycombDefinition</a>, ... ]</i>,
        "<a href="#loggingkafka" title="LoggingKafka">LoggingKafka</a>" : <i>[ <a href="loggingkafkadefinition.md">LoggingKafkaDefinition</a>, ... ]</i>,
        "<a href="#loggingkinesis" title="LoggingKinesis">LoggingKinesis</a>" : <i>[ <a href="loggingkinesisdefinition.md">LoggingKinesisDefinition</a>, ... ]</i>,
        "<a href="#loggingloggly" title="LoggingLoggly">LoggingLoggly</a>" : <i>[ <a href="logginglogglydefinition.md">LoggingLogglyDefinition</a>, ... ]</i>,
        "<a href="#logginglogshuttle" title="LoggingLogshuttle">LoggingLogshuttle</a>" : <i>[ <a href="logginglogshuttledefinition.md">LoggingLogshuttleDefinition</a>, ... ]</i>,
        "<a href="#loggingnewrelic" title="LoggingNewrelic">LoggingNewrelic</a>" : <i>[ <a href="loggingnewrelicdefinition.md">LoggingNewrelicDefinition</a>, ... ]</i>,
        "<a href="#loggingopenstack" title="LoggingOpenstack">LoggingOpenstack</a>" : <i>[ <a href="loggingopenstackdefinition.md">LoggingOpenstackDefinition</a>, ... ]</i>,
        "<a href="#loggingscalyr" title="LoggingScalyr">LoggingScalyr</a>" : <i>[ <a href="loggingscalyrdefinition.md">LoggingScalyrDefinition</a>, ... ]</i>,
        "<a href="#loggingsftp" title="LoggingSftp">LoggingSftp</a>" : <i>[ <a href="loggingsftpdefinition.md">LoggingSftpDefinition</a>, ... ]</i>,
        "<a href="#papertrail" title="Papertrail">Papertrail</a>" : <i>[ <a href="papertraildefinition.md">PapertrailDefinition</a>, ... ]</i>,
        "<a href="#requestsetting" title="RequestSetting">RequestSetting</a>" : <i>[ <a href="requestsettingdefinition.md">RequestSettingDefinition</a>, ... ]</i>,
        "<a href="#responseobject" title="ResponseObject">ResponseObject</a>" : <i>[ <a href="responseobjectdefinition.md">ResponseObjectDefinition</a>, ... ]</i>,
        "<a href="#s3logging" title="S3logging">S3logging</a>" : <i>[ <a href="s3loggingdefinition.md">S3loggingDefinition</a>, ... ]</i>,
        "<a href="#snippet" title="Snippet">Snippet</a>" : <i>[ <a href="snippetdefinition.md">SnippetDefinition</a>, ... ]</i>,
        "<a href="#splunk" title="Splunk">Splunk</a>" : <i>[ <a href="splunkdefinition.md">SplunkDefinition</a>, ... ]</i>,
        "<a href="#sumologic" title="Sumologic">Sumologic</a>" : <i>[ <a href="sumologicdefinition.md">SumologicDefinition</a>, ... ]</i>,
        "<a href="#syslog" title="Syslog">Syslog</a>" : <i>[ <a href="syslogdefinition.md">SyslogDefinition</a>, ... ]</i>,
        "<a href="#vcl" title="Vcl">Vcl</a>" : <i>[ <a href="vcldefinition.md">VclDefinition</a>, ... ]</i>,
        "<a href="#waf" title="Waf">Waf</a>" : <i>[ <a href="wafdefinition.md">WafDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::ServiceV1
Properties:
    <a href="#activate" title="Activate">Activate</a>: <i>Boolean</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#defaulthost" title="DefaultHost">DefaultHost</a>: <i>String</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versioncomment" title="VersionComment">VersionComment</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backenddefinition.md">BackendDefinition</a></i>
    <a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>: <i>
      - <a href="bigqueryloggingdefinition.md">BigqueryloggingDefinition</a></i>
    <a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>: <i>
      - <a href="blobstorageloggingdefinition.md">BlobstorageloggingDefinition</a></i>
    <a href="#cachesetting" title="CacheSetting">CacheSetting</a>: <i>
      - <a href="cachesettingdefinition.md">CacheSettingDefinition</a></i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
    <a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - <a href="dictionarydefinition.md">DictionaryDefinition</a></i>
    <a href="#director" title="Director">Director</a>: <i>
      - <a href="directordefinition.md">DirectorDefinition</a></i>
    <a href="#domain" title="Domain">Domain</a>: <i>
      - <a href="domaindefinition.md">DomainDefinition</a></i>
    <a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>: <i>
      - <a href="dynamicsnippetdefinition.md">DynamicsnippetDefinition</a></i>
    <a href="#gcslogging" title="Gcslogging">Gcslogging</a>: <i>
      - <a href="gcsloggingdefinition.md">GcsloggingDefinition</a></i>
    <a href="#gzip" title="Gzip">Gzip</a>: <i>
      - <a href="gzipdefinition.md">GzipDefinition</a></i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthcheckDefinition</a></i>
    <a href="#httpslogging" title="Httpslogging">Httpslogging</a>: <i>
      - <a href="httpsloggingdefinition.md">HttpsloggingDefinition</a></i>
    <a href="#logentries" title="Logentries">Logentries</a>: <i>
      - <a href="logentriesdefinition.md">LogentriesDefinition</a></i>
    <a href="#loggingcloudfiles" title="LoggingCloudfiles">LoggingCloudfiles</a>: <i>
      - <a href="loggingcloudfilesdefinition.md">LoggingCloudfilesDefinition</a></i>
    <a href="#loggingdatadog" title="LoggingDatadog">LoggingDatadog</a>: <i>
      - <a href="loggingdatadogdefinition.md">LoggingDatadogDefinition</a></i>
    <a href="#loggingdigitalocean" title="LoggingDigitalocean">LoggingDigitalocean</a>: <i>
      - <a href="loggingdigitaloceandefinition.md">LoggingDigitaloceanDefinition</a></i>
    <a href="#loggingelasticsearch" title="LoggingElasticsearch">LoggingElasticsearch</a>: <i>
      - <a href="loggingelasticsearchdefinition.md">LoggingElasticsearchDefinition</a></i>
    <a href="#loggingftp" title="LoggingFtp">LoggingFtp</a>: <i>
      - <a href="loggingftpdefinition.md">LoggingFtpDefinition</a></i>
    <a href="#logginggooglepubsub" title="LoggingGooglepubsub">LoggingGooglepubsub</a>: <i>
      - <a href="logginggooglepubsubdefinition.md">LoggingGooglepubsubDefinition</a></i>
    <a href="#loggingheroku" title="LoggingHeroku">LoggingHeroku</a>: <i>
      - <a href="loggingherokudefinition.md">LoggingHerokuDefinition</a></i>
    <a href="#logginghoneycomb" title="LoggingHoneycomb">LoggingHoneycomb</a>: <i>
      - <a href="logginghoneycombdefinition.md">LoggingHoneycombDefinition</a></i>
    <a href="#loggingkafka" title="LoggingKafka">LoggingKafka</a>: <i>
      - <a href="loggingkafkadefinition.md">LoggingKafkaDefinition</a></i>
    <a href="#loggingkinesis" title="LoggingKinesis">LoggingKinesis</a>: <i>
      - <a href="loggingkinesisdefinition.md">LoggingKinesisDefinition</a></i>
    <a href="#loggingloggly" title="LoggingLoggly">LoggingLoggly</a>: <i>
      - <a href="logginglogglydefinition.md">LoggingLogglyDefinition</a></i>
    <a href="#logginglogshuttle" title="LoggingLogshuttle">LoggingLogshuttle</a>: <i>
      - <a href="logginglogshuttledefinition.md">LoggingLogshuttleDefinition</a></i>
    <a href="#loggingnewrelic" title="LoggingNewrelic">LoggingNewrelic</a>: <i>
      - <a href="loggingnewrelicdefinition.md">LoggingNewrelicDefinition</a></i>
    <a href="#loggingopenstack" title="LoggingOpenstack">LoggingOpenstack</a>: <i>
      - <a href="loggingopenstackdefinition.md">LoggingOpenstackDefinition</a></i>
    <a href="#loggingscalyr" title="LoggingScalyr">LoggingScalyr</a>: <i>
      - <a href="loggingscalyrdefinition.md">LoggingScalyrDefinition</a></i>
    <a href="#loggingsftp" title="LoggingSftp">LoggingSftp</a>: <i>
      - <a href="loggingsftpdefinition.md">LoggingSftpDefinition</a></i>
    <a href="#papertrail" title="Papertrail">Papertrail</a>: <i>
      - <a href="papertraildefinition.md">PapertrailDefinition</a></i>
    <a href="#requestsetting" title="RequestSetting">RequestSetting</a>: <i>
      - <a href="requestsettingdefinition.md">RequestSettingDefinition</a></i>
    <a href="#responseobject" title="ResponseObject">ResponseObject</a>: <i>
      - <a href="responseobjectdefinition.md">ResponseObjectDefinition</a></i>
    <a href="#s3logging" title="S3logging">S3logging</a>: <i>
      - <a href="s3loggingdefinition.md">S3loggingDefinition</a></i>
    <a href="#snippet" title="Snippet">Snippet</a>: <i>
      - <a href="snippetdefinition.md">SnippetDefinition</a></i>
    <a href="#splunk" title="Splunk">Splunk</a>: <i>
      - <a href="splunkdefinition.md">SplunkDefinition</a></i>
    <a href="#sumologic" title="Sumologic">Sumologic</a>: <i>
      - <a href="sumologicdefinition.md">SumologicDefinition</a></i>
    <a href="#syslog" title="Syslog">Syslog</a>: <i>
      - <a href="syslogdefinition.md">SyslogDefinition</a></i>
    <a href="#vcl" title="Vcl">Vcl</a>: <i>
      - <a href="vcldefinition.md">VclDefinition</a></i>
    <a href="#waf" title="Waf">Waf</a>: <i>
      - <a href="wafdefinition.md">WafDefinition</a></i>
</pre>

## Properties

#### Activate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionComment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backenddefinition.md">BackendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bigquerylogging

_Required_: No

_Type_: List of <a href="bigqueryloggingdefinition.md">BigqueryloggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blobstoragelogging

_Required_: No

_Type_: List of <a href="blobstorageloggingdefinition.md">BlobstorageloggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheSetting

_Required_: No

_Type_: List of <a href="cachesettingdefinition.md">CacheSettingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of <a href="dictionarydefinition.md">DictionaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Director

_Required_: No

_Type_: List of <a href="directordefinition.md">DirectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of <a href="domaindefinition.md">DomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamicsnippet

_Required_: No

_Type_: List of <a href="dynamicsnippetdefinition.md">DynamicsnippetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gcslogging

_Required_: No

_Type_: List of <a href="gcsloggingdefinition.md">GcsloggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gzip

_Required_: No

_Type_: List of <a href="gzipdefinition.md">GzipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthcheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httpslogging

_Required_: No

_Type_: List of <a href="httpsloggingdefinition.md">HttpsloggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logentries

_Required_: No

_Type_: List of <a href="logentriesdefinition.md">LogentriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingCloudfiles

_Required_: No

_Type_: List of <a href="loggingcloudfilesdefinition.md">LoggingCloudfilesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingDatadog

_Required_: No

_Type_: List of <a href="loggingdatadogdefinition.md">LoggingDatadogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingDigitalocean

_Required_: No

_Type_: List of <a href="loggingdigitaloceandefinition.md">LoggingDigitaloceanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingElasticsearch

_Required_: No

_Type_: List of <a href="loggingelasticsearchdefinition.md">LoggingElasticsearchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingFtp

_Required_: No

_Type_: List of <a href="loggingftpdefinition.md">LoggingFtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingGooglepubsub

_Required_: No

_Type_: List of <a href="logginggooglepubsubdefinition.md">LoggingGooglepubsubDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingHeroku

_Required_: No

_Type_: List of <a href="loggingherokudefinition.md">LoggingHerokuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingHoneycomb

_Required_: No

_Type_: List of <a href="logginghoneycombdefinition.md">LoggingHoneycombDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingKafka

_Required_: No

_Type_: List of <a href="loggingkafkadefinition.md">LoggingKafkaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingKinesis

_Required_: No

_Type_: List of <a href="loggingkinesisdefinition.md">LoggingKinesisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingLoggly

_Required_: No

_Type_: List of <a href="logginglogglydefinition.md">LoggingLogglyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingLogshuttle

_Required_: No

_Type_: List of <a href="logginglogshuttledefinition.md">LoggingLogshuttleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingNewrelic

_Required_: No

_Type_: List of <a href="loggingnewrelicdefinition.md">LoggingNewrelicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingOpenstack

_Required_: No

_Type_: List of <a href="loggingopenstackdefinition.md">LoggingOpenstackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingScalyr

_Required_: No

_Type_: List of <a href="loggingscalyrdefinition.md">LoggingScalyrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingSftp

_Required_: No

_Type_: List of <a href="loggingsftpdefinition.md">LoggingSftpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Papertrail

_Required_: No

_Type_: List of <a href="papertraildefinition.md">PapertrailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSetting

_Required_: No

_Type_: List of <a href="requestsettingdefinition.md">RequestSettingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseObject

_Required_: No

_Type_: List of <a href="responseobjectdefinition.md">ResponseObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3logging

_Required_: No

_Type_: List of <a href="s3loggingdefinition.md">S3loggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snippet

_Required_: No

_Type_: List of <a href="snippetdefinition.md">SnippetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Splunk

_Required_: No

_Type_: List of <a href="splunkdefinition.md">SplunkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sumologic

_Required_: No

_Type_: List of <a href="sumologicdefinition.md">SumologicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Syslog

_Required_: No

_Type_: List of <a href="syslogdefinition.md">SyslogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcl

_Required_: No

_Type_: List of <a href="vcldefinition.md">VclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

_Required_: No

_Type_: List of <a href="wafdefinition.md">WafDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActiveVersion

Returns the <code>ActiveVersion</code> value.

#### ClonedVersion

Returns the <code>ClonedVersion</code> value.

#### Id

Returns the <code>Id</code> value.

