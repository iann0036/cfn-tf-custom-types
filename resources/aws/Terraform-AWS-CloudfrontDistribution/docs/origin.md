# Terraform::AWS::CloudfrontDistribution Origin

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
    "<a href="#originpath" title="OriginPath">OriginPath</a>" : <i>String</i>,
    "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>[ <a href="origin-customheader.md">CustomHeader</a>, ... ]</i>,
    "<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>" : <i>[ <a href="origin-customoriginconfig.md">CustomOriginConfig</a>, ... ]</i>,
    "<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>" : <i>[ <a href="origin-s3originconfig.md">S3OriginConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
<a href="#originpath" title="OriginPath">OriginPath</a>: <i>String</i>
<a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>
      - <a href="origin-customheader.md">CustomHeader</a></i>
<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>: <i>
      - <a href="origin-customoriginconfig.md">CustomOriginConfig</a></i>
<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>: <i>
      - <a href="origin-s3originconfig.md">S3OriginConfig</a></i>
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
_Type_: List of <a href="origin-customheader.md">CustomHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOriginConfig

_Required_: No
_Type_: List of <a href="origin-customoriginconfig.md">CustomOriginConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3OriginConfig

_Required_: No
_Type_: List of <a href="origin-s3originconfig.md">S3OriginConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

