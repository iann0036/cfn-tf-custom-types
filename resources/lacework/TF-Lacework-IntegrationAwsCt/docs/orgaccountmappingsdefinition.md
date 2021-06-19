# TF::Lacework::IntegrationAwsCt OrgAccountMappingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultlaceworkaccount" title="DefaultLaceworkAccount">DefaultLaceworkAccount</a>" : <i>String</i>,
    "<a href="#mapping" title="Mapping">Mapping</a>" : <i>[ <a href="mappingdefinition.md">MappingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultlaceworkaccount" title="DefaultLaceworkAccount">DefaultLaceworkAccount</a>: <i>String</i>
<a href="#mapping" title="Mapping">Mapping</a>: <i>
      - <a href="mappingdefinition.md">MappingDefinition</a></i>
</pre>

## Properties

#### DefaultLaceworkAccount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mapping

_Required_: No

_Type_: List of <a href="mappingdefinition.md">MappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

