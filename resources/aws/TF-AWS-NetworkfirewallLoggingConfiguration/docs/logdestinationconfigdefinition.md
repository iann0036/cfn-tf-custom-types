# TF::AWS::NetworkfirewallLoggingConfiguration LogDestinationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#logdestination" title="LogDestination">LogDestination</a>" : <i>[ <a href="logdestinationdefinition.md">LogDestinationDefinition</a>, ... ]</i>,
    "<a href="#logdestinationtype" title="LogDestinationType">LogDestinationType</a>" : <i>String</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#logdestination" title="LogDestination">LogDestination</a>: <i>
      - <a href="logdestinationdefinition.md">LogDestinationDefinition</a></i>
<a href="#logdestinationtype" title="LogDestinationType">LogDestinationType</a>: <i>String</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
</pre>

## Properties

#### LogDestination

_Required_: Yes

_Type_: List of <a href="logdestinationdefinition.md">LogDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDestinationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

