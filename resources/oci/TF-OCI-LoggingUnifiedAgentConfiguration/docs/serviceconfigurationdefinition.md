# TF::OCI::LoggingUnifiedAgentConfiguration ServiceConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destinationdefinition.md">DestinationDefinition</a>, ... ]</i>,
    "<a href="#sources" title="Sources">Sources</a>" : <i>[ <a href="sourcesdefinition.md">SourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destinationdefinition.md">DestinationDefinition</a></i>
<a href="#sources" title="Sources">Sources</a>: <i>
      - <a href="sourcesdefinition.md">SourcesDefinition</a></i>
</pre>

## Properties

#### ConfigurationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destinationdefinition.md">DestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

_Required_: No

_Type_: List of <a href="sourcesdefinition.md">SourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

