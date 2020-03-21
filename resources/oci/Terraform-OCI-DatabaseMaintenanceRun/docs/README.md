# Terraform::OCI::DatabaseMaintenanceRun

CloudFormation equivalent of oci_database_maintenance_run

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseMaintenanceRun",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#maintenancerunid" title="MaintenanceRunId">MaintenanceRunId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseMaintenanceRun
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#maintenancerunid" title="MaintenanceRunId">MaintenanceRunId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceRunId

_Required_: Yes

_Type_: String

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

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### MaintenanceSubtype

Returns the &lt;code&gt;MaintenanceSubtype&lt;/code&gt; value.

#### MaintenanceType

Returns the &lt;code&gt;MaintenanceType&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TargetResourceId

Returns the &lt;code&gt;TargetResourceId&lt;/code&gt; value.

#### TargetResourceType

Returns the &lt;code&gt;TargetResourceType&lt;/code&gt; value.

#### TimeEnded

Returns the &lt;code&gt;TimeEnded&lt;/code&gt; value.

#### TimeScheduled

Returns the &lt;code&gt;TimeScheduled&lt;/code&gt; value.

#### TimeStarted

Returns the &lt;code&gt;TimeStarted&lt;/code&gt; value.

