# Terraform::Fastly::ServiceV1

CloudFormation equivalent of fastly_service_v1

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versioncomment" title="VersionComment">VersionComment</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
        "<a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>" : <i>[ &lt;a href=&#34;bigquerylogging.md&#34;&gt;Bigquerylogging&lt;/a&gt;, ... ]</i>,
        "<a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>" : <i>[ &lt;a href=&#34;blobstoragelogging.md&#34;&gt;Blobstoragelogging&lt;/a&gt;, ... ]</i>,
        "<a href="#cachesetting" title="CacheSetting">CacheSetting</a>" : <i>[ &lt;a href=&#34;cachesetting.md&#34;&gt;CacheSetting&lt;/a&gt;, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
        "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ &lt;a href=&#34;dictionary.md&#34;&gt;Dictionary&lt;/a&gt;, ... ]</i>,
        "<a href="#director" title="Director">Director</a>" : <i>[ &lt;a href=&#34;director.md&#34;&gt;Director&lt;/a&gt;, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>[ &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>" : <i>[ &lt;a href=&#34;dynamicsnippet.md&#34;&gt;Dynamicsnippet&lt;/a&gt;, ... ]</i>,
        "<a href="#gcslogging" title="Gcslogging">Gcslogging</a>" : <i>[ &lt;a href=&#34;gcslogging.md&#34;&gt;Gcslogging&lt;/a&gt;, ... ]</i>,
        "<a href="#gzip" title="Gzip">Gzip</a>" : <i>[ &lt;a href=&#34;gzip.md&#34;&gt;Gzip&lt;/a&gt;, ... ]</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;, ... ]</i>,
        "<a href="#logentries" title="Logentries">Logentries</a>" : <i>[ &lt;a href=&#34;logentries.md&#34;&gt;Logentries&lt;/a&gt;, ... ]</i>,
        "<a href="#papertrail" title="Papertrail">Papertrail</a>" : <i>[ &lt;a href=&#34;papertrail.md&#34;&gt;Papertrail&lt;/a&gt;, ... ]</i>,
        "<a href="#requestsetting" title="RequestSetting">RequestSetting</a>" : <i>[ &lt;a href=&#34;requestsetting.md&#34;&gt;RequestSetting&lt;/a&gt;, ... ]</i>,
        "<a href="#responseobject" title="ResponseObject">ResponseObject</a>" : <i>[ &lt;a href=&#34;responseobject.md&#34;&gt;ResponseObject&lt;/a&gt;, ... ]</i>,
        "<a href="#s3logging" title="S3logging">S3logging</a>" : <i>[ &lt;a href=&#34;s3logging.md&#34;&gt;S3logging&lt;/a&gt;, ... ]</i>,
        "<a href="#snippet" title="Snippet">Snippet</a>" : <i>[ &lt;a href=&#34;snippet.md&#34;&gt;Snippet&lt;/a&gt;, ... ]</i>,
        "<a href="#splunk" title="Splunk">Splunk</a>" : <i>[ &lt;a href=&#34;splunk.md&#34;&gt;Splunk&lt;/a&gt;, ... ]</i>,
        "<a href="#sumologic" title="Sumologic">Sumologic</a>" : <i>[ &lt;a href=&#34;sumologic.md&#34;&gt;Sumologic&lt;/a&gt;, ... ]</i>,
        "<a href="#syslog" title="Syslog">Syslog</a>" : <i>[ &lt;a href=&#34;syslog.md&#34;&gt;Syslog&lt;/a&gt;, ... ]</i>,
        "<a href="#vcl" title="Vcl">Vcl</a>" : <i>[ &lt;a href=&#34;vcl.md&#34;&gt;Vcl&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versioncomment" title="VersionComment">VersionComment</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;</i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;</i>
    <a href="#bigquerylogging" title="Bigquerylogging">Bigquerylogging</a>: <i>
      - &lt;a href=&#34;bigquerylogging.md&#34;&gt;Bigquerylogging&lt;/a&gt;</i>
    <a href="#blobstoragelogging" title="Blobstoragelogging">Blobstoragelogging</a>: <i>
      - &lt;a href=&#34;blobstoragelogging.md&#34;&gt;Blobstoragelogging&lt;/a&gt;</i>
    <a href="#cachesetting" title="CacheSetting">CacheSetting</a>: <i>
      - &lt;a href=&#34;cachesetting.md&#34;&gt;CacheSetting&lt;/a&gt;</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
    <a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - &lt;a href=&#34;dictionary.md&#34;&gt;Dictionary&lt;/a&gt;</i>
    <a href="#director" title="Director">Director</a>: <i>
      - &lt;a href=&#34;director.md&#34;&gt;Director&lt;/a&gt;</i>
    <a href="#domain" title="Domain">Domain</a>: <i>
      - &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;</i>
    <a href="#dynamicsnippet" title="Dynamicsnippet">Dynamicsnippet</a>: <i>
      - &lt;a href=&#34;dynamicsnippet.md&#34;&gt;Dynamicsnippet&lt;/a&gt;</i>
    <a href="#gcslogging" title="Gcslogging">Gcslogging</a>: <i>
      - &lt;a href=&#34;gcslogging.md&#34;&gt;Gcslogging&lt;/a&gt;</i>
    <a href="#gzip" title="Gzip">Gzip</a>: <i>
      - &lt;a href=&#34;gzip.md&#34;&gt;Gzip&lt;/a&gt;</i>
    <a href="#header" title="Header">Header</a>: <i>
      - &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;</i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;</i>
    <a href="#logentries" title="Logentries">Logentries</a>: <i>
      - &lt;a href=&#34;logentries.md&#34;&gt;Logentries&lt;/a&gt;</i>
    <a href="#papertrail" title="Papertrail">Papertrail</a>: <i>
      - &lt;a href=&#34;papertrail.md&#34;&gt;Papertrail&lt;/a&gt;</i>
    <a href="#requestsetting" title="RequestSetting">RequestSetting</a>: <i>
      - &lt;a href=&#34;requestsetting.md&#34;&gt;RequestSetting&lt;/a&gt;</i>
    <a href="#responseobject" title="ResponseObject">ResponseObject</a>: <i>
      - &lt;a href=&#34;responseobject.md&#34;&gt;ResponseObject&lt;/a&gt;</i>
    <a href="#s3logging" title="S3logging">S3logging</a>: <i>
      - &lt;a href=&#34;s3logging.md&#34;&gt;S3logging&lt;/a&gt;</i>
    <a href="#snippet" title="Snippet">Snippet</a>: <i>
      - &lt;a href=&#34;snippet.md&#34;&gt;Snippet&lt;/a&gt;</i>
    <a href="#splunk" title="Splunk">Splunk</a>: <i>
      - &lt;a href=&#34;splunk.md&#34;&gt;Splunk&lt;/a&gt;</i>
    <a href="#sumologic" title="Sumologic">Sumologic</a>: <i>
      - &lt;a href=&#34;sumologic.md&#34;&gt;Sumologic&lt;/a&gt;</i>
    <a href="#syslog" title="Syslog">Syslog</a>: <i>
      - &lt;a href=&#34;syslog.md&#34;&gt;Syslog&lt;/a&gt;</i>
    <a href="#vcl" title="Vcl">Vcl</a>: <i>
      - &lt;a href=&#34;vcl.md&#34;&gt;Vcl&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

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

_Type_: List of &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bigquerylogging

_Required_: No

_Type_: List of &lt;a href=&#34;bigquerylogging.md&#34;&gt;Bigquerylogging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blobstoragelogging

_Required_: No

_Type_: List of &lt;a href=&#34;blobstoragelogging.md&#34;&gt;Blobstoragelogging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheSetting

_Required_: No

_Type_: List of &lt;a href=&#34;cachesetting.md&#34;&gt;CacheSetting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of &lt;a href=&#34;dictionary.md&#34;&gt;Dictionary&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Director

_Required_: No

_Type_: List of &lt;a href=&#34;director.md&#34;&gt;Director&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamicsnippet

_Required_: No

_Type_: List of &lt;a href=&#34;dynamicsnippet.md&#34;&gt;Dynamicsnippet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gcslogging

_Required_: No

_Type_: List of &lt;a href=&#34;gcslogging.md&#34;&gt;Gcslogging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gzip

_Required_: No

_Type_: List of &lt;a href=&#34;gzip.md&#34;&gt;Gzip&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheck.md&#34;&gt;Healthcheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logentries

_Required_: No

_Type_: List of &lt;a href=&#34;logentries.md&#34;&gt;Logentries&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Papertrail

_Required_: No

_Type_: List of &lt;a href=&#34;papertrail.md&#34;&gt;Papertrail&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSetting

_Required_: No

_Type_: List of &lt;a href=&#34;requestsetting.md&#34;&gt;RequestSetting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseObject

_Required_: No

_Type_: List of &lt;a href=&#34;responseobject.md&#34;&gt;ResponseObject&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3logging

_Required_: No

_Type_: List of &lt;a href=&#34;s3logging.md&#34;&gt;S3logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snippet

_Required_: No

_Type_: List of &lt;a href=&#34;snippet.md&#34;&gt;Snippet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Splunk

_Required_: No

_Type_: List of &lt;a href=&#34;splunk.md&#34;&gt;Splunk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sumologic

_Required_: No

_Type_: List of &lt;a href=&#34;sumologic.md&#34;&gt;Sumologic&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Syslog

_Required_: No

_Type_: List of &lt;a href=&#34;syslog.md&#34;&gt;Syslog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcl

_Required_: No

_Type_: List of &lt;a href=&#34;vcl.md&#34;&gt;Vcl&lt;/a&gt;

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

Returns the &lt;code&gt;ActiveVersion&lt;/code&gt; value.

#### ClonedVersion

Returns the &lt;code&gt;ClonedVersion&lt;/code&gt; value.

