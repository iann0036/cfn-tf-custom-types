# TF::AWS::Kinesisanalyticsv2Application PropertyGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#propertygroupid" title="PropertyGroupId">PropertyGroupId</a>" : <i>String</i>,
    "<a href="#propertymap" title="PropertyMap">PropertyMap</a>" : <i>[ <a href="propertymapdefinition.md">PropertyMapDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#propertygroupid" title="PropertyGroupId">PropertyGroupId</a>: <i>String</i>
<a href="#propertymap" title="PropertyMap">PropertyMap</a>: <i>
      - <a href="propertymapdefinition.md">PropertyMapDefinition</a></i>
</pre>

## Properties

#### PropertyGroupId

The key of the application execution property key-value map.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyMap

Application execution property key-value map.

_Required_: Yes

_Type_: List of <a href="propertymapdefinition.md">PropertyMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

