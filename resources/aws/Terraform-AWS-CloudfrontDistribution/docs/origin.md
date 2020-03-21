# Terraform::AWS::CloudfrontDistribution Origin

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
    "<a href="#originpath" title="OriginPath">OriginPath</a>" : <i>String</i>,
    "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>[ &lt;a href=&#34;origin-customheader.md&#34;&gt;CustomHeader&lt;/a&gt;, ... ]</i>,
    "<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>" : <i>[ &lt;a href=&#34;origin-customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>" : <i>[ &lt;a href=&#34;origin-s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
<a href="#originpath" title="OriginPath">OriginPath</a>: <i>String</i>
<a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>
      - &lt;a href=&#34;origin-customheader.md&#34;&gt;CustomHeader&lt;/a&gt;</i>
<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>: <i>
      - &lt;a href=&#34;origin-customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;</i>
<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>: <i>
      - &lt;a href=&#34;origin-s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;</i>
</pre>

## Properties

#### DomainName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPath

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeader

_Required_: No
_Type_: List of &lt;a href=&#34;origin-customheader.md&#34;&gt;CustomHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOriginConfig

_Required_: No
_Type_: List of &lt;a href=&#34;origin-customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3OriginConfig

_Required_: No
_Type_: List of &lt;a href=&#34;origin-s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

