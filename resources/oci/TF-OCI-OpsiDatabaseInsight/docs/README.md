# TF::OCI::OpsiDatabaseInsight

This resource provides the Database Insight resource in Oracle Cloud Infrastructure Opsi service.

Create a Database Insight resource for a Enterprise Manager(EM) managed database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started. The Database Insight resource for Autonomous Database and Management Agent managed external Database needs to be created by Database service terraform provider.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OpsiDatabaseInsight",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#enterprisemanagerbridgeid" title="EnterpriseManagerBridgeId">EnterpriseManagerBridgeId</a>" : <i>String</i>,
        "<a href="#enterprisemanagerentityidentifier" title="EnterpriseManagerEntityIdentifier">EnterpriseManagerEntityIdentifier</a>" : <i>String</i>,
        "<a href="#enterprisemanageridentifier" title="EnterpriseManagerIdentifier">EnterpriseManagerIdentifier</a>" : <i>String</i>,
        "<a href="#entitysource" title="EntitySource">EntitySource</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OpsiDatabaseInsight
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#enterprisemanagerbridgeid" title="EnterpriseManagerBridgeId">EnterpriseManagerBridgeId</a>: <i>String</i>
    <a href="#enterprisemanagerentityidentifier" title="EnterpriseManagerEntityIdentifier">EnterpriseManagerEntityIdentifier</a>: <i>String</i>
    <a href="#enterprisemanageridentifier" title="EnterpriseManagerIdentifier">EnterpriseManagerIdentifier</a>: <i>String</i>
    <a href="#entitysource" title="EntitySource">EntitySource</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) Compartment Identifier of database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseManagerBridgeId

OPSI Enterprise Manager Bridge OCID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseManagerEntityIdentifier

Enterprise Manager Entity Unique Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseManagerIdentifier

Enterprise Manager Unqiue Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntitySource

(Updatable) Source of the database entity. The supported type is "EM_MANAGED_EXTERNAL_DATABASE".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

(Updatable) Status of the resource. Example: "ENABLED", "DISABLED". Resource can be either enabled or disabled by updating the value of status field to either "ENABLED" or "DISABLED".

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

#### DatabaseDisplayName

Returns the <code>DatabaseDisplayName</code> value.

#### DatabaseId

Returns the <code>DatabaseId</code> value.

#### DatabaseName

Returns the <code>DatabaseName</code> value.

#### DatabaseType

Returns the <code>DatabaseType</code> value.

#### DatabaseVersion

Returns the <code>DatabaseVersion</code> value.

#### EnterpriseManagerEntityDisplayName

Returns the <code>EnterpriseManagerEntityDisplayName</code> value.

#### EnterpriseManagerEntityName

Returns the <code>EnterpriseManagerEntityName</code> value.

#### EnterpriseManagerEntityType

Returns the <code>EnterpriseManagerEntityType</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### ProcessorCount

Returns the <code>ProcessorCount</code> value.

#### State

Returns the <code>State</code> value.

#### SystemTags

Returns the <code>SystemTags</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

