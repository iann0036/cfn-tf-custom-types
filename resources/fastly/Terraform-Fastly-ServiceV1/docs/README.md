# Terraform::Fastly::ServiceV1

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
    "Type" : "Terraform::Fastly::ServiceV1",
    "Properties" : {
        "<a href="#activate" title="Activate">Activate</a>" : <i>Boolean</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#defaulthost" title="DefaultHost">DefaultHost</a>" : <i>String</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versioncomment" title="VersionComment">VersionComment</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acl.md">Acl</a>, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backend.md">Backend</a>, ... ]</i>,
        "<a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>" : <i>[ <a href="bigquerylogging.md">Bigquerylogging</a>, ... ]</i>,
        "<a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>" : <i>[ <a href="blobstoragelogging.md">Blobstoragelogging</a>, ... ]</i>,
        "<a href="#cachesetting" title="CacheSetting">CacheSetting</a>" : <i>[ <a href="cachesetting.md">CacheSetting</a>, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="condition.md">Condition</a>, ... ]</i>,
        "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ <a href="dictionary.md">Dictionary</a>, ... ]</i>,
        "<a href="#director" title="Director">Director</a>" : <i>[ <a href="director.md">Director</a>, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>[ <a href="domain.md">Domain</a>, ... ]</i>,
        "<a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>" : <i>[ <a href="dynamicsnippet.md">Dynamicsnippet</a>, ... ]</i>,
        "<a href="#gcslogging" title="Gcslogging">Gcslogging</a>" : <i>[ <a href="gcslogging.md">Gcslogging</a>, ... ]</i>,
        "<a href="#gzip" title="Gzip">Gzip</a>" : <i>[ <a href="gzip.md">Gzip</a>, ... ]</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="header.md">Header</a>, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheck.md">Healthcheck</a>, ... ]</i>,
        "<a href="#logentries" title="Logentries">Logentries</a>" : <i>[ <a href="logentries.md">Logentries</a>, ... ]</i>,
        "<a href="#papertrail" title="Papertrail">Papertrail</a>" : <i>[ <a href="papertrail.md">Papertrail</a>, ... ]</i>,
        "<a href="#requestsetting" title="RequestSetting">RequestSetting</a>" : <i>[ <a href="requestsetting.md">RequestSetting</a>, ... ]</i>,
        "<a href="#responseobject" title="ResponseObject">ResponseObject</a>" : <i>[ <a href="responseobject.md">ResponseObject</a>, ... ]</i>,
        "<a href="#s3logging" title="S3logging">S3logging</a>" : <i>[ <a href="s3logging.md">S3logging</a>, ... ]</i>,
        "<a href="#snippet" title="Snippet">Snippet</a>" : <i>[ <a href="snippet.md">Snippet</a>, ... ]</i>,
        "<a href="#splunk" title="Splunk">Splunk</a>" : <i>[ <a href="splunk.md">Splunk</a>, ... ]</i>,
        "<a href="#sumologic" title="Sumologic">Sumologic</a>" : <i>[ <a href="sumologic.md">Sumologic</a>, ... ]</i>,
        "<a href="#syslog" title="Syslog">Syslog</a>" : <i>[ <a href="syslog.md">Syslog</a>, ... ]</i>,
        "<a href="#vcl" title="Vcl">Vcl</a>" : <i>[ <a href="vcl.md">Vcl</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Fastly::ServiceV1
Properties:
    <a href="#activate" title="Activate">Activate</a>: <i>Boolean</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#defaulthost" title="DefaultHost">DefaultHost</a>: <i>String</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versioncomment" title="VersionComment">VersionComment</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acl.md">Acl</a></i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backend.md">Backend</a></i>
    <a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>: <i>
      - <a href="bigquerylogging.md">Bigquerylogging</a></i>
    <a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>: <i>
      - <a href="blobstoragelogging.md">Blobstoragelogging</a></i>
    <a href="#cachesetting" title="CacheSetting">CacheSetting</a>: <i>
      - <a href="cachesetting.md">CacheSetting</a></i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="condition.md">Condition</a></i>
    <a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - <a href="dictionary.md">Dictionary</a></i>
    <a href="#director" title="Director">Director</a>: <i>
      - <a href="director.md">Director</a></i>
    <a href="#domain" title="Domain">Domain</a>: <i>
      - <a href="domain.md">Domain</a></i>
    <a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>: <i>
      - <a href="dynamicsnippet.md">Dynamicsnippet</a></i>
    <a href="#gcslogging" title="Gcslogging">Gcslogging</a>: <i>
      - <a href="gcslogging.md">Gcslogging</a></i>
    <a href="#gzip" title="Gzip">Gzip</a>: <i>
      - <a href="gzip.md">Gzip</a></i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="header.md">Header</a></i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheck.md">Healthcheck</a></i>
    <a href="#logentries" title="Logentries">Logentries</a>: <i>
      - <a href="logentries.md">Logentries</a></i>
    <a href="#papertrail" title="Papertrail">Papertrail</a>: <i>
      - <a href="papertrail.md">Papertrail</a></i>
    <a href="#requestsetting" title="RequestSetting">RequestSetting</a>: <i>
      - <a href="requestsetting.md">RequestSetting</a></i>
    <a href="#responseobject" title="ResponseObject">ResponseObject</a>: <i>
      - <a href="responseobject.md">ResponseObject</a></i>
    <a href="#s3logging" title="S3logging">S3logging</a>: <i>
      - <a href="s3logging.md">S3logging</a></i>
    <a href="#snippet" title="Snippet">Snippet</a>: <i>
      - <a href="snippet.md">Snippet</a></i>
    <a href="#splunk" title="Splunk">Splunk</a>: <i>
      - <a href="splunk.md">Splunk</a></i>
    <a href="#sumologic" title="Sumologic">Sumologic</a>: <i>
      - <a href="sumologic.md">Sumologic</a></i>
    <a href="#syslog" title="Syslog">Syslog</a>: <i>
      - <a href="syslog.md">Syslog</a></i>
    <a href="#vcl" title="Vcl">Vcl</a>: <i>
      - <a href="vcl.md">Vcl</a></i>
</pre>

## Properties

#### Activate

Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Description field for the service. Default `Managed by Terraform`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHost

The default hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

The default Time-to-live (TTL) for
requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

Services that are active cannot be destroyed. In
order to destroy the Service, set `force_destroy` to `true`. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name for the Service to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionComment

Description field for the version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acl.md">Acl</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bigquerylogging

_Required_: No

_Type_: List of <a href="bigquerylogging.md">Bigquerylogging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blobstoragelogging

_Required_: No

_Type_: List of <a href="blobstoragelogging.md">Blobstoragelogging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheSetting

_Required_: No

_Type_: List of <a href="cachesetting.md">CacheSetting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of <a href="dictionary.md">Dictionary</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Director

_Required_: No

_Type_: List of <a href="director.md">Director</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of <a href="domain.md">Domain</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamicsnippet

_Required_: No

_Type_: List of <a href="dynamicsnippet.md">Dynamicsnippet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gcslogging

_Required_: No

_Type_: List of <a href="gcslogging.md">Gcslogging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gzip

_Required_: No

_Type_: List of <a href="gzip.md">Gzip</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheck.md">Healthcheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logentries

_Required_: No

_Type_: List of <a href="logentries.md">Logentries</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Papertrail

_Required_: No

_Type_: List of <a href="papertrail.md">Papertrail</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSetting

_Required_: No

_Type_: List of <a href="requestsetting.md">RequestSetting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseObject

_Required_: No

_Type_: List of <a href="responseobject.md">ResponseObject</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3logging

_Required_: No

_Type_: List of <a href="s3logging.md">S3logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snippet

_Required_: No

_Type_: List of <a href="snippet.md">Snippet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Splunk

_Required_: No

_Type_: List of <a href="splunk.md">Splunk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sumologic

_Required_: No

_Type_: List of <a href="sumologic.md">Sumologic</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Syslog

_Required_: No

_Type_: List of <a href="syslog.md">Syslog</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcl

_Required_: No

_Type_: List of <a href="vcl.md">Vcl</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

