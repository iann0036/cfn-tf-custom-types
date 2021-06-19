# TF::Alicloud::CdnDomain

-> **DEPRECATED:**  This resource is based on CDN's old version OpenAPI and it has been deprecated from version `1.34.0`.
Please use new resource [alicloud_cdn_domain_new](https://www.terraform.io/docs/providers/alicloud/r/cdn_domain_new.html) and its
config [alicloud_cdn_domain_config](https://www.terraform.io/docs/providers/alicloud/r/cdn_domain_config.html) instead.

Provides a CDN Accelerated Domain resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CdnDomain",
    "Properties" : {
        "<a href="#blockips" title="BlockIps">BlockIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#cdntype" title="CdnType">CdnType</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#optimizeenable" title="OptimizeEnable">OptimizeEnable</a>" : <i>String</i>,
        "<a href="#pagecompressenable" title="PageCompressEnable">PageCompressEnable</a>" : <i>String</i>,
        "<a href="#rangeenable" title="RangeEnable">RangeEnable</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>Double</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#sources" title="Sources">Sources</a>" : <i>[ String, ... ]</i>,
        "<a href="#videoseekenable" title="VideoSeekEnable">VideoSeekEnable</a>" : <i>String</i>,
        "<a href="#authconfig" title="AuthConfig">AuthConfig</a>" : <i>[ <a href="authconfigdefinition.md">AuthConfigDefinition</a>, ... ]</i>,
        "<a href="#cacheconfig" title="CacheConfig">CacheConfig</a>" : <i>[ <a href="cacheconfigdefinition.md">CacheConfigDefinition</a>, ... ]</i>,
        "<a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>" : <i>[ <a href="certificateconfigdefinition.md">CertificateConfigDefinition</a>, ... ]</i>,
        "<a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>" : <i>[ <a href="httpheaderconfigdefinition.md">HttpHeaderConfigDefinition</a>, ... ]</i>,
        "<a href="#page404config" title="Page404Config">Page404Config</a>" : <i>[ <a href="page404configdefinition.md">Page404ConfigDefinition</a>, ... ]</i>,
        "<a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>" : <i>[ <a href="parameterfilterconfigdefinition.md">ParameterFilterConfigDefinition</a>, ... ]</i>,
        "<a href="#referconfig" title="ReferConfig">ReferConfig</a>" : <i>[ <a href="referconfigdefinition.md">ReferConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CdnDomain
Properties:
    <a href="#blockips" title="BlockIps">BlockIps</a>: <i>
      - String</i>
    <a href="#cdntype" title="CdnType">CdnType</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#optimizeenable" title="OptimizeEnable">OptimizeEnable</a>: <i>String</i>
    <a href="#pagecompressenable" title="PageCompressEnable">PageCompressEnable</a>: <i>String</i>
    <a href="#rangeenable" title="RangeEnable">RangeEnable</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#sourceport" title="SourcePort">SourcePort</a>: <i>Double</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
    <a href="#sources" title="Sources">Sources</a>: <i>
      - String</i>
    <a href="#videoseekenable" title="VideoSeekEnable">VideoSeekEnable</a>: <i>String</i>
    <a href="#authconfig" title="AuthConfig">AuthConfig</a>: <i>
      - <a href="authconfigdefinition.md">AuthConfigDefinition</a></i>
    <a href="#cacheconfig" title="CacheConfig">CacheConfig</a>: <i>
      - <a href="cacheconfigdefinition.md">CacheConfigDefinition</a></i>
    <a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>: <i>
      - <a href="certificateconfigdefinition.md">CertificateConfigDefinition</a></i>
    <a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>: <i>
      - <a href="httpheaderconfigdefinition.md">HttpHeaderConfigDefinition</a></i>
    <a href="#page404config" title="Page404Config">Page404Config</a>: <i>
      - <a href="page404configdefinition.md">Page404ConfigDefinition</a></i>
    <a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>: <i>
      - <a href="parameterfilterconfigdefinition.md">ParameterFilterConfigDefinition</a></i>
    <a href="#referconfig" title="ReferConfig">ReferConfig</a>: <i>
      - <a href="referconfigdefinition.md">ReferConfigDefinition</a></i>
</pre>

## Properties

#### BlockIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnType

Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizeEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageCompressEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoSeekEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthConfig

_Required_: No

_Type_: List of <a href="authconfigdefinition.md">AuthConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheConfig

_Required_: No

_Type_: List of <a href="cacheconfigdefinition.md">CacheConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateConfig

_Required_: No

_Type_: List of <a href="certificateconfigdefinition.md">CertificateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaderConfig

_Required_: No

_Type_: List of <a href="httpheaderconfigdefinition.md">HttpHeaderConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Page404Config

_Required_: No

_Type_: List of <a href="page404configdefinition.md">Page404ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterFilterConfig

_Required_: No

_Type_: List of <a href="parameterfilterconfigdefinition.md">ParameterFilterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferConfig

_Required_: No

_Type_: List of <a href="referconfigdefinition.md">ReferConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

