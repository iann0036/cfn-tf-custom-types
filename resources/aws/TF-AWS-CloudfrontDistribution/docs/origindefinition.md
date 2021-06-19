# TF::AWS::CloudfrontDistribution OriginDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionattempts" title="ConnectionAttempts">ConnectionAttempts</a>" : <i>Double</i>,
    "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
    "<a href="#originpath" title="OriginPath">OriginPath</a>" : <i>String</i>,
    "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>[ <a href="customheaderdefinition.md">CustomHeaderDefinition</a>, ... ]</i>,
    "<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>" : <i>[ <a href="customoriginconfigdefinition.md">CustomOriginConfigDefinition</a>, ... ]</i>,
    "<a href="#originshield" title="OriginShield">OriginShield</a>" : <i>[ <a href="originshielddefinition.md">OriginShieldDefinition</a>, ... ]</i>,
    "<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>" : <i>[ <a href="s3originconfigdefinition.md">S3OriginConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectionattempts" title="ConnectionAttempts">ConnectionAttempts</a>: <i>Double</i>
<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
<a href="#originpath" title="OriginPath">OriginPath</a>: <i>String</i>
<a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>
      - <a href="customheaderdefinition.md">CustomHeaderDefinition</a></i>
<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>: <i>
      - <a href="customoriginconfigdefinition.md">CustomOriginConfigDefinition</a></i>
<a href="#originshield" title="OriginShield">OriginShield</a>: <i>
      - <a href="originshielddefinition.md">OriginShieldDefinition</a></i>
<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>: <i>
      - <a href="s3originconfigdefinition.md">S3OriginConfigDefinition</a></i>
</pre>

## Properties

#### ConnectionAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of <a href="customheaderdefinition.md">CustomHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOriginConfig

_Required_: No

_Type_: List of <a href="customoriginconfigdefinition.md">CustomOriginConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginShield

_Required_: No

_Type_: List of <a href="originshielddefinition.md">OriginShieldDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3OriginConfig

_Required_: No

_Type_: List of <a href="s3originconfigdefinition.md">S3OriginConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

