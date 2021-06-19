# TF::Google::ProjectDefaultServiceAccounts

Allows management of Google Cloud Platform project default service accounts.

When certain service APIs are enabled, Google Cloud Platform automatically creates service accounts to help get started, but
this is not recommended for production environments as per [Google's documentation](https://cloud.google.com/iam/docs/service-accounts#default).
See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

~> **WARNING** Some Google Cloud products do not work if the default service accounts are deleted so it is better to `DEPRIVILEGE` as
Google **CAN NOT** recover service accounts that have been deleted for more than 30 days.
Also Google recommends using the `constraints/iam.automaticIamGrantsForDefaultServiceAccounts` [constraint](/docs/providers/google/r/google_organization_policy.html)
to disable automatic IAM Grants to default service accounts.

~> This resource works on a best-effort basis, as no API formally describes the default service accounts...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ProjectDefaultServiceAccounts",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ProjectDefaultServiceAccounts
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Action

The action to be performed in the default service accounts. Valid values are: `DEPRIVILEGE`, `DELETE`, `DISABLE`. Note that `DEPRIVILEGE` action will ignore the REVERT configuration in the restore_policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project ID where service accounts are created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePolicy

The action to be performed in the default service accounts on the resource destroy.
Valid values are NONE, REVERT and REVERT_AND_IGNORE_FAILURE. It is applied for any action but in the DEPRIVILEGE.
If set to REVERT it attempts to restore all default SAs but the DEPRIVILEGE action.
If set to REVERT_AND_IGNORE_FAILURE it is the same behavior as REVERT but ignores errors returned by the API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### ServiceAccounts

Returns the <code>ServiceAccounts</code> value.

