# Terraform::FlexibleEngine::RdsInstanceV1

Manages rds instance resource within FlexibleEngine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::RdsInstanceV1",
    "Properties" : {
        "<a href="#availabilityzone" title="Availabilityzone">Availabilityzone</a>" : <i>String</i>,
        "<a href="#created" title="Created">Created</a>" : <i>String</i>,
        "<a href="#dbport" title="Dbport">Dbport</a>" : <i>String</i>,
        "<a href="#dbrtpd" title="Dbrtpd">Dbrtpd</a>" : <i>String</i>,
        "<a href="#flavorref" title="Flavorref">Flavorref</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#updated" title="Updated">Updated</a>" : <i>String</i>,
        "<a href="#vpc" title="Vpc">Vpc</a>" : <i>String</i>,
        "<a href="#backupstrategy" title="Backupstrategy">Backupstrategy</a>" : <i>[ <a href="backupstrategy.md">Backupstrategy</a>, ... ]</i>,
        "<a href="#datastore" title="Datastore">Datastore</a>" : <i>[ <a href="datastore.md">Datastore</a>, ... ]</i>,
        "<a href="#ha" title="Ha">Ha</a>" : <i>[ <a href="ha.md">Ha</a>, ... ]</i>,
        "<a href="#nics" title="Nics">Nics</a>" : <i>[ <a href="nics.md">Nics</a>, ... ]</i>,
        "<a href="#securitygroup" title="Securitygroup">Securitygroup</a>" : <i>[ <a href="securitygroup.md">Securitygroup</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::RdsInstanceV1
Properties:
    <a href="#availabilityzone" title="Availabilityzone">Availabilityzone</a>: <i>String</i>
    <a href="#created" title="Created">Created</a>: <i>String</i>
    <a href="#dbport" title="Dbport">Dbport</a>: <i>String</i>
    <a href="#dbrtpd" title="Dbrtpd">Dbrtpd</a>: <i>String</i>
    <a href="#flavorref" title="Flavorref">Flavorref</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#updated" title="Updated">Updated</a>: <i>String</i>
    <a href="#vpc" title="Vpc">Vpc</a>: <i>String</i>
    <a href="#backupstrategy" title="Backupstrategy">Backupstrategy</a>: <i>
      - <a href="backupstrategy.md">Backupstrategy</a></i>
    <a href="#datastore" title="Datastore">Datastore</a>: <i>
      - <a href="datastore.md">Datastore</a></i>
    <a href="#ha" title="Ha">Ha</a>: <i>
      - <a href="ha.md">Ha</a></i>
    <a href="#nics" title="Nics">Nics</a>: <i>
      - <a href="nics.md">Nics</a></i>
    <a href="#securitygroup" title="Securitygroup">Securitygroup</a>: <i>
      - <a href="securitygroup.md">Securitygroup</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
</pre>

## Properties

#### Availabilityzone

Specifies the ID of the AZ.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Created

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dbport

Specifies the database port number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dbrtpd

Specifies the password for user root of the database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavorref

Specifies the specification ID (flavors.id in the
response message in Obtaining All DB Instance Specifications). If you want
to enable ha for the rds instance, a flavor with ha speccode is required.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the DB instance name. The DB instance name of
the same type is unique in the same tenant. The changes of the instance name
will be suppressed in HA scenario.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Specifies the region ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Updated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

Specifies the VPC ID. For details about how to obtain this
parameter value, see section "Virtual Private Cloud" in the Virtual Private
Cloud API Reference.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backupstrategy

_Required_: No

_Type_: List of <a href="backupstrategy.md">Backupstrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datastore

_Required_: No

_Type_: List of <a href="datastore.md">Datastore</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ha

_Required_: No

_Type_: List of <a href="ha.md">Ha</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nics

_Required_: No

_Type_: List of <a href="nics.md">Nics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Securitygroup

_Required_: No

_Type_: List of <a href="securitygroup.md">Securitygroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

