# TF::Nutanix::RecoveryPlan EntityInfoListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anyentityreferencekind" title="AnyEntityReferenceKind">AnyEntityReferenceKind</a>" : <i>String</i>,
    "<a href="#anyentityreferencename" title="AnyEntityReferenceName">AnyEntityReferenceName</a>" : <i>String</i>,
    "<a href="#anyentityreferenceuuid" title="AnyEntityReferenceUuid">AnyEntityReferenceUuid</a>" : <i>String</i>,
    "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
    "<a href="#scriptlist" title="ScriptList">ScriptList</a>" : <i>[ <a href="scriptlistdefinition.md">ScriptListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anyentityreferencekind" title="AnyEntityReferenceKind">AnyEntityReferenceKind</a>: <i>String</i>
<a href="#anyentityreferencename" title="AnyEntityReferenceName">AnyEntityReferenceName</a>: <i>String</i>
<a href="#anyentityreferenceuuid" title="AnyEntityReferenceUuid">AnyEntityReferenceUuid</a>: <i>String</i>
<a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
<a href="#scriptlist" title="ScriptList">ScriptList</a>: <i>
      - <a href="scriptlistdefinition.md">ScriptListDefinition</a></i>
</pre>

## Properties

#### AnyEntityReferenceKind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyEntityReferenceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyEntityReferenceUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptList

_Required_: No

_Type_: List of <a href="scriptlistdefinition.md">ScriptListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

