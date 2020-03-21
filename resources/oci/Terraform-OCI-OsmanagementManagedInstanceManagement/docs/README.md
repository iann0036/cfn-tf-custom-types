# Terraform::OCI::OsmanagementManagedInstanceManagement

CloudFormation equivalent of oci_osmanagement_managed_instance_management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::OsmanagementManagedInstanceManagement",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#managedinstanceid" title="ManagedInstanceId">ManagedInstanceId</a>" : <i>String</i>,
        "<a href="#childsoftwaresources" title="ChildSoftwareSources">ChildSoftwareSources</a>" : <i>[ <a href="childsoftwaresources.md">ChildSoftwareSources</a>, ... ]</i>,
        "<a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>" : <i>[ <a href="managedinstancegroups.md">ManagedInstanceGroups</a>, ... ]</i>,
        "<a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>" : <i>[ <a href="parentsoftwaresource.md">ParentSoftwareSource</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::OsmanagementManagedInstanceManagement
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#managedinstanceid" title="ManagedInstanceId">ManagedInstanceId</a>: <i>String</i>
    <a href="#childsoftwaresources" title="ChildSoftwareSources">ChildSoftwareSources</a>: <i>
      - <a href="childsoftwaresources.md">ChildSoftwareSources</a></i>
    <a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>: <i>
      - <a href="managedinstancegroups.md">ManagedInstanceGroups</a></i>
    <a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>: <i>
      - <a href="parentsoftwaresource.md">ParentSoftwareSource</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedInstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildSoftwareSources

_Required_: No

_Type_: List of <a href="childsoftwaresources.md">ChildSoftwareSources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedInstanceGroups

_Required_: No

_Type_: List of <a href="managedinstancegroups.md">ManagedInstanceGroups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentSoftwareSource

_Required_: No

_Type_: List of <a href="parentsoftwaresource.md">ParentSoftwareSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Description

Returns the <code>Description</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### LastBoot

Returns the <code>LastBoot</code> value.

#### LastCheckin

Returns the <code>LastCheckin</code> value.

#### OsKernelVersion

Returns the <code>OsKernelVersion</code> value.

#### OsName

Returns the <code>OsName</code> value.

#### OsVersion

Returns the <code>OsVersion</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatesAvailable

Returns the <code>UpdatesAvailable</code> value.

