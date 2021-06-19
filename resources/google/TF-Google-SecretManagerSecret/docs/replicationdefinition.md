# TF::Google::SecretManagerSecret ReplicationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automatic" title="Automatic">Automatic</a>" : <i>Boolean</i>,
    "<a href="#usermanaged" title="UserManaged">UserManaged</a>" : <i>[ <a href="usermanageddefinition.md">UserManagedDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automatic" title="Automatic">Automatic</a>: <i>Boolean</i>
<a href="#usermanaged" title="UserManaged">UserManaged</a>: <i>
      - <a href="usermanageddefinition.md">UserManagedDefinition</a></i>
</pre>

## Properties

#### Automatic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserManaged

_Required_: No

_Type_: List of <a href="usermanageddefinition.md">UserManagedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

