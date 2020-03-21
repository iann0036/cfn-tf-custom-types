# Terraform::AzureRM::CosmosdbAccount GeoLocation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#failoverpriority" title="FailoverPriority">FailoverPriority</a>" : <i>Double</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#failoverpriority" title="FailoverPriority">FailoverPriority</a>: <i>Double</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
</pre>

## Properties

#### FailoverPriority

The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The name of the Azure region to host replicated data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

