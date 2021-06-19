# TF::OCI::DatabaseAutonomousContainerDatabaseDataguardAssociationOperation

This resource provides the Autonomous Container Database Dataguard Association Operation resource in Oracle Cloud Infrastructure Database service.

Perform a new Autonomous Container Database Dataguard Association Operation on an Autonomous Container Database that has Dataguard enabled

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseAutonomousContainerDatabaseDataguardAssociationOperation",
    "Properties" : {
        "<a href="#autonomouscontainerdatabasedataguardassociationid" title="AutonomousContainerDatabaseDataguardAssociationId">AutonomousContainerDatabaseDataguardAssociationId</a>" : <i>String</i>,
        "<a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>" : <i>String</i>,
        "<a href="#operation" title="Operation">Operation</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseAutonomousContainerDatabaseDataguardAssociationOperation
Properties:
    <a href="#autonomouscontainerdatabasedataguardassociationid" title="AutonomousContainerDatabaseDataguardAssociationId">AutonomousContainerDatabaseDataguardAssociationId</a>: <i>String</i>
    <a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>: <i>String</i>
    <a href="#operation" title="Operation">Operation</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutonomousContainerDatabaseDataguardAssociationId

The Autonomous Container Database Dataguard Association [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This attribute is a forcenew attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousContainerDatabaseId

The Autonomous Container Database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). This attribute is a forcenew attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operation

There are three type of supported operations `switchover`, `failover`, `reinstate`. `switchover` can only be used for primary database while `failover` and `reinstate` can only be used for standby database. This attribute is a forcenew attribute.

_Required_: Yes

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

