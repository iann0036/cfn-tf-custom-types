# TF::OCI::OsmanagementManagedInstanceManagement

This resource provides the Managed Instance Management in Oracle Cloud Infrastructure OS Management service.
The resource can be used to attach/detach parent software source, child software sources and managed instance groups from managed instances.

Adds a parent software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance. Software sources that have this software source as a parent will be able to be added to this managed instance.
Removes a software source from a managed instance. All child software sources will also be removed from the managed instance. Packages will no longer be able to be installed from these software sources.
        
Adds a child software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance.   
Removes a child software source from a managed instance. Packages will no longer be able t...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OsmanagementManagedInstanceManagement",
    "Properties" : {
        "<a href="#managedinstanceid" title="ManagedInstanceId">ManagedInstanceId</a>" : <i>String</i>,
        "<a href="#childsoftwaresources" title="ChildSoftwareSources">ChildSoftwareSources</a>" : <i>[ <a href="childsoftwaresourcesdefinition.md">ChildSoftwareSourcesDefinition</a>, ... ]</i>,
        "<a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>" : <i>[ <a href="managedinstancegroupsdefinition.md">ManagedInstanceGroupsDefinition</a>, ... ]</i>,
        "<a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>" : <i>[ <a href="parentsoftwaresourcedefinition.md">ParentSoftwareSourceDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OsmanagementManagedInstanceManagement
Properties:
    <a href="#managedinstanceid" title="ManagedInstanceId">ManagedInstanceId</a>: <i>String</i>
    <a href="#childsoftwaresources" title="ChildSoftwareSources">ChildSoftwareSources</a>: <i>
      - <a href="childsoftwaresourcesdefinition.md">ChildSoftwareSourcesDefinition</a></i>
    <a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>: <i>
      - <a href="managedinstancegroupsdefinition.md">ManagedInstanceGroupsDefinition</a></i>
    <a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>: <i>
      - <a href="parentsoftwaresourcedefinition.md">ParentSoftwareSourceDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ManagedInstanceId

OCID for the managed instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildSoftwareSources

_Required_: No

_Type_: List of <a href="childsoftwaresourcesdefinition.md">ChildSoftwareSourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedInstanceGroups

_Required_: No

_Type_: List of <a href="managedinstancegroupsdefinition.md">ManagedInstanceGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentSoftwareSource

_Required_: No

_Type_: List of <a href="parentsoftwaresourcedefinition.md">ParentSoftwareSourceDefinition</a>

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

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Description

Returns the <code>Description</code> value.

#### DisplayName

User friendly name
* `id` - unique identifier that is immutable on creation.

#### Id

software source identifier
* `name` - software source name.

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

