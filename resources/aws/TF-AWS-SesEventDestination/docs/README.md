# TF::AWS::SesEventDestination

Provides an SES event destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SesEventDestination",
    "Properties" : {
        "<a href="#configurationsetname" title="ConfigurationSetName">ConfigurationSetName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#matchingtypes" title="MatchingTypes">MatchingTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#cloudwatchdestination" title="CloudwatchDestination">CloudwatchDestination</a>" : <i>[ <a href="cloudwatchdestinationdefinition.md">CloudwatchDestinationDefinition</a>, ... ]</i>,
        "<a href="#kinesisdestination" title="KinesisDestination">KinesisDestination</a>" : <i>[ <a href="kinesisdestinationdefinition.md">KinesisDestinationDefinition</a>, ... ]</i>,
        "<a href="#snsdestination" title="SnsDestination">SnsDestination</a>" : <i>[ <a href="snsdestinationdefinition.md">SnsDestinationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SesEventDestination
Properties:
    <a href="#configurationsetname" title="ConfigurationSetName">ConfigurationSetName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#matchingtypes" title="MatchingTypes">MatchingTypes</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#cloudwatchdestination" title="CloudwatchDestination">CloudwatchDestination</a>: <i>
      - <a href="cloudwatchdestinationdefinition.md">CloudwatchDestinationDefinition</a></i>
    <a href="#kinesisdestination" title="KinesisDestination">KinesisDestination</a>: <i>
      - <a href="kinesisdestinationdefinition.md">KinesisDestinationDefinition</a></i>
    <a href="#snsdestination" title="SnsDestination">SnsDestination</a>: <i>
      - <a href="snsdestinationdefinition.md">SnsDestinationDefinition</a></i>
</pre>

## Properties

#### ConfigurationSetName

The name of the configuration set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

If true, the event destination will be enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchingTypes

A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the event destination.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchDestination

_Required_: No

_Type_: List of <a href="cloudwatchdestinationdefinition.md">CloudwatchDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisDestination

_Required_: No

_Type_: List of <a href="kinesisdestinationdefinition.md">KinesisDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsDestination

_Required_: No

_Type_: List of <a href="snsdestinationdefinition.md">SnsDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

