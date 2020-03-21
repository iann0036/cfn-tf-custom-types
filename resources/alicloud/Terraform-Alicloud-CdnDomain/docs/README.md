# Terraform::Alicloud::CdnDomain

CloudFormation equivalent of alicloud_cdn_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CdnDomain",
    "Properties" : {
        "<a href="#blockips" title="BlockIps">BlockIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#cdntype" title="CdnType">CdnType</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#optimizeenable" title="OptimizeEnable">OptimizeEnable</a>" : <i>String</i>,
        "<a href="#pagecompressenable" title="PageCompressEnable">PageCompressEnable</a>" : <i>String</i>,
        "<a href="#rangeenable" title="RangeEnable">RangeEnable</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>Double</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#sources" title="Sources">Sources</a>" : <i>[ String, ... ]</i>,
        "<a href="#videoseekenable" title="VideoSeekEnable">VideoSeekEnable</a>" : <i>String</i>,
        "<a href="#authconfig" title="AuthConfig">AuthConfig</a>" : <i>[ <a href="authconfig.md">AuthConfig</a>, ... ]</i>,
        "<a href="#cacheconfig" title="CacheConfig">CacheConfig</a>" : <i>[ <a href="cacheconfig.md">CacheConfig</a>, ... ]</i>,
        "<a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>" : <i>[ <a href="certificateconfig.md">CertificateConfig</a>, ... ]</i>,
        "<a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>" : <i>[ <a href="httpheaderconfig.md">HttpHeaderConfig</a>, ... ]</i>,
        "<a href="#page404config" title="Page404Config">Page404Config</a>" : <i>[ <a href="page404config.md">Page404Config</a>, ... ]</i>,
        "<a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>" : <i>[ <a href="parameterfilterconfig.md">ParameterFilterConfig</a>, ... ]</i>,
        "<a href="#referconfig" title="ReferConfig">ReferConfig</a>" : <i>[ <a href="referconfig.md">ReferConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CdnDomain
Properties:
    <a href="#blockips" title="BlockIps">BlockIps</a>: <i>
      - String</i>
    <a href="#cdntype" title="CdnType">CdnType</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
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
      - <a href="authconfig.md">AuthConfig</a></i>
    <a href="#cacheconfig" title="CacheConfig">CacheConfig</a>: <i>
      - <a href="cacheconfig.md">CacheConfig</a></i>
    <a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>: <i>
      - <a href="certificateconfig.md">CertificateConfig</a></i>
    <a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>: <i>
      - <a href="httpheaderconfig.md">HttpHeaderConfig</a></i>
    <a href="#page404config" title="Page404Config">Page404Config</a>: <i>
      - <a href="page404config.md">Page404Config</a></i>
    <a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>: <i>
      - <a href="parameterfilterconfig.md">ParameterFilterConfig</a></i>
    <a href="#referconfig" title="ReferConfig">ReferConfig</a>: <i>
      - <a href="referconfig.md">ReferConfig</a></i>
</pre>

## Properties

#### BlockIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoSeekEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthConfig

_Required_: No

_Type_: List of <a href="authconfig.md">AuthConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheConfig

_Required_: No

_Type_: List of <a href="cacheconfig.md">CacheConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateConfig

_Required_: No

_Type_: List of <a href="certificateconfig.md">CertificateConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaderConfig

_Required_: No

_Type_: List of <a href="httpheaderconfig.md">HttpHeaderConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Page404Config

_Required_: No

_Type_: List of <a href="page404config.md">Page404Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterFilterConfig

_Required_: No

_Type_: List of <a href="parameterfilterconfig.md">ParameterFilterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferConfig

_Required_: No

_Type_: List of <a href="referconfig.md">ReferConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
