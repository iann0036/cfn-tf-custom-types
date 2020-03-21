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
        "<a href="#childsoftwaresources" title="ChildSoftwareSources">ChildSoftwareSources</a>" : <i>[ &lt;a href=&#34;childsoftwaresources.md&#34;&gt;ChildSoftwareSources&lt;/a&gt;, ... ]</i>,
        "<a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>" : <i>[ &lt;a href=&#34;managedinstancegroups.md&#34;&gt;ManagedInstanceGroups&lt;/a&gt;, ... ]</i>,
        "<a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>" : <i>[ &lt;a href=&#34;parentsoftwaresource.md&#34;&gt;ParentSoftwareSource&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
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
      - &lt;a href=&#34;childsoftwaresources.md&#34;&gt;ChildSoftwareSources&lt;/a&gt;</i>
    <a href="#managedinstancegroups" title="ManagedInstanceGroups">ManagedInstanceGroups</a>: <i>
      - &lt;a href=&#34;managedinstancegroups.md&#34;&gt;ManagedInstanceGroups&lt;/a&gt;</i>
    <a href="#parentsoftwaresource" title="ParentSoftwareSource">ParentSoftwareSource</a>: <i>
      - &lt;a href=&#34;parentsoftwaresource.md&#34;&gt;ParentSoftwareSource&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;childsoftwaresources.md&#34;&gt;ChildSoftwareSources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedInstanceGroups

_Required_: No

_Type_: List of &lt;a href=&#34;managedinstancegroups.md&#34;&gt;ManagedInstanceGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentSoftwareSource

_Required_: No

_Type_: List of &lt;a href=&#34;parentsoftwaresource.md&#34;&gt;ParentSoftwareSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;CompartmentId&lt;/code&gt; value.

#### Description

Returns the &lt;code&gt;Description&lt;/code&gt; value.

#### DisplayName

Returns the &lt;code&gt;DisplayName&lt;/code&gt; value.

#### LastBoot

Returns the &lt;code&gt;LastBoot&lt;/code&gt; value.

#### LastCheckin

Returns the &lt;code&gt;LastCheckin&lt;/code&gt; value.

#### OsKernelVersion

Returns the &lt;code&gt;OsKernelVersion&lt;/code&gt; value.

#### OsName

Returns the &lt;code&gt;OsName&lt;/code&gt; value.

#### OsVersion

Returns the &lt;code&gt;OsVersion&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### UpdatesAvailable

Returns the &lt;code&gt;UpdatesAvailable&lt;/code&gt; value.

