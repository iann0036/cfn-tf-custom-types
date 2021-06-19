# TF::Google::Project

Allows creation and management of a Google Cloud Platform project.

Projects created with this resource must be associated with an Organization.
See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The user or service account that is running Terraform when creating a `google_project`
resource must have `roles/resourcemanager.projectCreator` on the specified organization. See the
[Access Control for Organizations Using IAM](https://cloud.google.com/resource-manager/docs/access-control-org)
doc for more information.

~> This resource reads the specified billing account on every terraform apply and plan operation so you must have permissions on the specified billing account.

~> It is recommended to use the `constraints/compute.skipDefaultNetworkCreation` [constraint](/docs/providers/google/r/google_organization_policy.html) to remove the default network instead of setting `auto_create_network` to false.

To get more information about projects, s...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::Project",
    "Properties" : {
        "<a href="#autocreatenetwork" title="AutoCreateNetwork">AutoCreateNetwork</a>" : <i>Boolean</i>,
        "<a href="#billingaccount" title="BillingAccount">BillingAccount</a>" : <i>String</i>,
        "<a href="#folderid" title="FolderId">FolderId</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orgid" title="OrgId">OrgId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#skipdelete" title="SkipDelete">SkipDelete</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::Project
Properties:
    <a href="#autocreatenetwork" title="AutoCreateNetwork">AutoCreateNetwork</a>: <i>Boolean</i>
    <a href="#billingaccount" title="BillingAccount">BillingAccount</a>: <i>String</i>
    <a href="#folderid" title="FolderId">FolderId</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orgid" title="OrgId">OrgId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#skipdelete" title="SkipDelete">SkipDelete</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoCreateNetwork

Create the 'default' network automatically.  Default `true`.
If set to `false`, the default network will be deleted.  Note that, for quota purposes, you
will still need to have 1 network slot available to create the project successfully, even if
you set `auto_create_network` to `false`, since the network will exist momentarily.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingAccount

The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have at mininum Billing Account User privileges (`roles/billing.user`) on the billing account.
See [Google Cloud Billing API Access Control](https://cloud.google.com/billing/docs/how-to/billing-access)
for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FolderId

The numeric ID of the folder this project should be
created under. Only one of `org_id` or `folder_id` may be
specified. If the `folder_id` is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A set of key/value label pairs to assign to the project.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The display name of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgId

The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
`org_id` or `folder_id` may be specified. If the `org_id` is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID. Changing this forces a new project to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipDelete

If true, the Terraform resource can be deleted
without deleting the Project via the Google API.

_Required_: No

_Type_: Boolean

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

#### Number

Returns the <code>Number</code> value.

