# TF::Volterra::K8sClusterRoleBinding SubjectsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>[ <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>
      - <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a></i>
</pre>

## Properties

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: List of <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

