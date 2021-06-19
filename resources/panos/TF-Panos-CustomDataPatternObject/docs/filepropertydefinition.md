# TF::Panos::CustomDataPatternObject FilePropertyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fileproperty" title="FileProperty">FileProperty</a>" : <i>[ <a href="filepropertydefinition.md">FilePropertyDefinition</a>, ... ]</i>,
    "<a href="#filetype" title="FileType">FileType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#propertyvalue" title="PropertyValue">PropertyValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fileproperty" title="FileProperty">FileProperty</a>: <i>
      - <a href="filepropertydefinition.md">FilePropertyDefinition</a></i>
<a href="#filetype" title="FileType">FileType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#propertyvalue" title="PropertyValue">PropertyValue</a>: <i>String</i>
</pre>

## Properties

#### FileProperty

_Required_: Yes

_Type_: List of <a href="filepropertydefinition.md">FilePropertyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileType

The file type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyValue

Property value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

