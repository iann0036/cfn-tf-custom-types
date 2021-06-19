# TF::LaunchDarkly::Webhook PolicyStatementsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
    "<a href="#effect" title="Effect">Effect</a>" : <i>String</i>,
    "<a href="#notactions" title="NotActions">NotActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#notresources" title="NotResources">NotResources</a>" : <i>[ String, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
<a href="#effect" title="Effect">Effect</a>: <i>String</i>
<a href="#notactions" title="NotActions">NotActions</a>: <i>
      - String</i>
<a href="#notresources" title="NotResources">NotResources</a>: <i>
      - String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
</pre>

## Properties

#### Actions

The list of action specifiers defining the actions to which the statement applies. Either `actions` or `not_actions` must be specified. For a list of available actions read [Actions reference](https://docs.launchdarkly.com/home/account-security/custom-roles/actions#actions-reference).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Effect

Either `allow` or `deny`. This argument defines whether the statement allows or denies access to the named resources and actions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotActions

The list of action specifiers defining the actions to which the statement does not apply. Either `actions` or `not_actions` must be specified. For a list of available actions read [Actions reference](https://docs.launchdarkly.com/home/account-security/custom-roles/actions#actions-reference).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotResources

The list of resource specifiers defining the resources to which the statement does not apply. Either `resources` or `not_resources` must be specified. For a list of available resources read [Understanding resource types and scopes](https://docs.launchdarkly.com/home/account-security/custom-roles/resources#understanding-resource-types-and-scopes).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

The list of resource specifiers defining the resources to which the statement applies. Either `resources` or `not_resources` must be specified. For a list of available resources read [Understanding resource types and scopes](https://docs.launchdarkly.com/home/account-security/custom-roles/resources#understanding-resource-types-and-scopes).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

