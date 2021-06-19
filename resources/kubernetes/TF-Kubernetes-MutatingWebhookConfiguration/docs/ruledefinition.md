# TF::Kubernetes::MutatingWebhookConfiguration RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apigroups" title="ApiGroups">ApiGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#apiversions" title="ApiVersions">ApiVersions</a>" : <i>[ String, ... ]</i>,
    "<a href="#operations" title="Operations">Operations</a>" : <i>[ String, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#apigroups" title="ApiGroups">ApiGroups</a>: <i>
      - String</i>
<a href="#apiversions" title="ApiVersions">ApiVersions</a>: <i>
      - String</i>
<a href="#operations" title="Operations">Operations</a>: <i>
      - String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
</pre>

## Properties

#### ApiGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiVersions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

