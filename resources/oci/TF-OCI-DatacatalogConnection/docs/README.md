# TF::OCI::DatacatalogConnection

This resource provides the Connection resource in Oracle Cloud Infrastructure Data Catalog service.

Creates a new connection.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatacatalogConnection",
    "Properties" : {
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#dataassetkey" title="DataAssetKey">DataAssetKey</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#encproperties" title="EncProperties">EncProperties</a>" : <i>[ <a href="encpropertiesdefinition.md">EncPropertiesDefinition</a>, ... ]</i>,
        "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="propertiesdefinition.md">PropertiesDefinition</a>, ... ]</i>,
        "<a href="#typekey" title="TypeKey">TypeKey</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatacatalogConnection
Properties:
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#dataassetkey" title="DataAssetKey">DataAssetKey</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#encproperties" title="EncProperties">EncProperties</a>: <i>
      - <a href="encpropertiesdefinition.md">EncPropertiesDefinition</a></i>
    <a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="propertiesdefinition.md">PropertiesDefinition</a></i>
    <a href="#typekey" title="TypeKey">TypeKey</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CatalogId

Unique catalog identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataAssetKey

Unique data asset key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) A description of the connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncProperties

(Updatable) A map of maps that contains the encrypted values for sensitive properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the "default" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{"encProperties": { "default": { "password": "example-password"}}}`.

_Required_: No

_Type_: List of <a href="encpropertiesdefinition.md">EncPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

(Updatable) Indicates whether this connection is the default connection. The first connection of a data asset defaults to being the default, subsequent connections default to not being the default. If a default connection already exists, then trying to create a connection as the default will fail. In this case the default connection would need to be updated not to be the default and then the new connection can then be created as the default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

(Updatable) A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the "default" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{"properties": { "default": { "username": "user1"}}}` . Terraform treats all map of maps as a flattened map with `.` denoting each level. For more information check out this [example](https://github.com/terraform-providers/terraform-provider-oci/blob/master/examples/datacatalog/main.tf).

_Required_: Yes

_Type_: List of <a href="propertiesdefinition.md">PropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeKey

The key of the object type. Type key's can be found via the '/types' endpoint.

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

#### CreatedById

Returns the <code>CreatedById</code> value.

#### ExternalKey

Returns the <code>ExternalKey</code> value.

#### Id

Returns the <code>Id</code> value.

#### Key

Returns the <code>Key</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeStatusUpdated

Returns the <code>TimeStatusUpdated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

#### UpdatedById

Returns the <code>UpdatedById</code> value.

#### Uri

Returns the <code>Uri</code> value.

