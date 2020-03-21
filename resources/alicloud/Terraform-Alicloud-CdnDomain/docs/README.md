# Terraform::Alicloud::CdnDomain

CloudFormation equivalent of alicloud_cdn_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CdnDomain",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
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
        "<a href="#authconfig" title="AuthConfig">AuthConfig</a>" : <i>[ &lt;a href=&#34;authconfig.md&#34;&gt;AuthConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#cacheconfig" title="CacheConfig">CacheConfig</a>" : <i>[ &lt;a href=&#34;cacheconfig.md&#34;&gt;CacheConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>" : <i>[ &lt;a href=&#34;certificateconfig.md&#34;&gt;CertificateConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>" : <i>[ &lt;a href=&#34;httpheaderconfig.md&#34;&gt;HttpHeaderConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#page404config" title="Page404Config">Page404Config</a>" : <i>[ &lt;a href=&#34;page404config.md&#34;&gt;Page404Config&lt;/a&gt;, ... ]</i>,
        "<a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>" : <i>[ &lt;a href=&#34;parameterfilterconfig.md&#34;&gt;ParameterFilterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#referconfig" title="ReferConfig">ReferConfig</a>" : <i>[ &lt;a href=&#34;referconfig.md&#34;&gt;ReferConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CdnDomain
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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
      - &lt;a href=&#34;authconfig.md&#34;&gt;AuthConfig&lt;/a&gt;</i>
    <a href="#cacheconfig" title="CacheConfig">CacheConfig</a>: <i>
      - &lt;a href=&#34;cacheconfig.md&#34;&gt;CacheConfig&lt;/a&gt;</i>
    <a href="#certificateconfig" title="CertificateConfig">CertificateConfig</a>: <i>
      - &lt;a href=&#34;certificateconfig.md&#34;&gt;CertificateConfig&lt;/a&gt;</i>
    <a href="#httpheaderconfig" title="HttpHeaderConfig">HttpHeaderConfig</a>: <i>
      - &lt;a href=&#34;httpheaderconfig.md&#34;&gt;HttpHeaderConfig&lt;/a&gt;</i>
    <a href="#page404config" title="Page404Config">Page404Config</a>: <i>
      - &lt;a href=&#34;page404config.md&#34;&gt;Page404Config&lt;/a&gt;</i>
    <a href="#parameterfilterconfig" title="ParameterFilterConfig">ParameterFilterConfig</a>: <i>
      - &lt;a href=&#34;parameterfilterconfig.md&#34;&gt;ParameterFilterConfig&lt;/a&gt;</i>
    <a href="#referconfig" title="ReferConfig">ReferConfig</a>: <i>
      - &lt;a href=&#34;referconfig.md&#34;&gt;ReferConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;authconfig.md&#34;&gt;AuthConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheConfig

_Required_: No

_Type_: List of &lt;a href=&#34;cacheconfig.md&#34;&gt;CacheConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateConfig

_Required_: No

_Type_: List of &lt;a href=&#34;certificateconfig.md&#34;&gt;CertificateConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaderConfig

_Required_: No

_Type_: List of &lt;a href=&#34;httpheaderconfig.md&#34;&gt;HttpHeaderConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Page404Config

_Required_: No

_Type_: List of &lt;a href=&#34;page404config.md&#34;&gt;Page404Config&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterFilterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;parameterfilterconfig.md&#34;&gt;ParameterFilterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferConfig

_Required_: No

_Type_: List of &lt;a href=&#34;referconfig.md&#34;&gt;ReferConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

