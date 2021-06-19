# TF::Google::EventarcTrigger DestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudfunction" title="CloudFunction">CloudFunction</a>" : <i>String</i>,
    "<a href="#cloudrunservice" title="CloudRunService">CloudRunService</a>" : <i>[ <a href="cloudrunservicedefinition.md">CloudRunServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudfunction" title="CloudFunction">CloudFunction</a>: <i>String</i>
<a href="#cloudrunservice" title="CloudRunService">CloudRunService</a>: <i>
      - <a href="cloudrunservicedefinition.md">CloudRunServiceDefinition</a></i>
</pre>

## Properties

#### CloudFunction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRunService

_Required_: No

_Type_: List of <a href="cloudrunservicedefinition.md">CloudRunServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

