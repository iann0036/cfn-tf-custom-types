# TF::Rancher2::RoleTemplate RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apigroups" title="ApiGroups">ApiGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#nonresourceurls" title="NonResourceUrls">NonResourceUrls</a>" : <i>[ String, ... ]</i>,
    "<a href="#resourcenames" title="ResourceNames">ResourceNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
    "<a href="#verbs" title="Verbs">Verbs</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apigroups" title="ApiGroups">ApiGroups</a>: <i>
      - String</i>
<a href="#nonresourceurls" title="NonResourceUrls">NonResourceUrls</a>: <i>
      - String</i>
<a href="#resourcenames" title="ResourceNames">ResourceNames</a>: <i>
      - String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
<a href="#verbs" title="Verbs">Verbs</a>: <i>
      - String</i>
</pre>

## Properties

#### ApiGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonResourceUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Verbs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

