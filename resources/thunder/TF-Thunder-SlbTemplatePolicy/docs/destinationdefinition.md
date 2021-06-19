# TF::Thunder::SlbTemplatePolicy DestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#any" title="Any">Any</a>" : <i>[ <a href="anydefinition.md">AnyDefinition</a>, ... ]</i>,
    "<a href="#classlistlist" title="ClassListList">ClassListList</a>" : <i>[ <a href="classlistlistdefinition.md">ClassListListDefinition</a>, ... ]</i>,
    "<a href="#webcategorylistlist" title="WebCategoryListList">WebCategoryListList</a>" : <i>[ <a href="webcategorylistlistdefinition.md">WebCategoryListListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#any" title="Any">Any</a>: <i>
      - <a href="anydefinition.md">AnyDefinition</a></i>
<a href="#classlistlist" title="ClassListList">ClassListList</a>: <i>
      - <a href="classlistlistdefinition.md">ClassListListDefinition</a></i>
<a href="#webcategorylistlist" title="WebCategoryListList">WebCategoryListList</a>: <i>
      - <a href="webcategorylistlistdefinition.md">WebCategoryListListDefinition</a></i>
</pre>

## Properties

#### Any

_Required_: No

_Type_: List of <a href="anydefinition.md">AnyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassListList

_Required_: No

_Type_: List of <a href="classlistlistdefinition.md">ClassListListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebCategoryListList

_Required_: No

_Type_: List of <a href="webcategorylistlistdefinition.md">WebCategoryListListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

