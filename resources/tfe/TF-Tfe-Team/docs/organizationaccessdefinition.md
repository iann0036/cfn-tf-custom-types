# TF::Tfe::Team OrganizationAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#managepolicies" title="ManagePolicies">ManagePolicies</a>" : <i>Boolean</i>,
    "<a href="#managepolicyoverrides" title="ManagePolicyOverrides">ManagePolicyOverrides</a>" : <i>Boolean</i>,
    "<a href="#managevcssettings" title="ManageVcsSettings">ManageVcsSettings</a>" : <i>Boolean</i>,
    "<a href="#manageworkspaces" title="ManageWorkspaces">ManageWorkspaces</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#managepolicies" title="ManagePolicies">ManagePolicies</a>: <i>Boolean</i>
<a href="#managepolicyoverrides" title="ManagePolicyOverrides">ManagePolicyOverrides</a>: <i>Boolean</i>
<a href="#managevcssettings" title="ManageVcsSettings">ManageVcsSettings</a>: <i>Boolean</i>
<a href="#manageworkspaces" title="ManageWorkspaces">ManageWorkspaces</a>: <i>Boolean</i>
</pre>

## Properties

#### ManagePolicies

Allows members to create, edit, and delete the organization's Sentinel policies.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagePolicyOverrides

Allows members to override soft-mandatory policy checks.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageVcsSettings

Allows members to manage the organization's VCS Providers and SSH keys.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageWorkspaces

Allows members to create and administrate all workspaces within the organization.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

