# TF::AzureRM::SpringCloudAppCosmosdbAssociation

Associates a [Spring Cloud Application](spring_cloud_app.html) with a [CosmosDB Account](cosmosdb_account.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SpringCloudAppCosmosdbAssociation",
    "Properties" : {
        "<a href="#apitype" title="ApiType">ApiType</a>" : <i>String</i>,
        "<a href="#cosmosdbaccesskey" title="CosmosdbAccessKey">CosmosdbAccessKey</a>" : <i>String</i>,
        "<a href="#cosmosdbaccountid" title="CosmosdbAccountId">CosmosdbAccountId</a>" : <i>String</i>,
        "<a href="#cosmosdbcassandrakeyspacename" title="CosmosdbCassandraKeyspaceName">CosmosdbCassandraKeyspaceName</a>" : <i>String</i>,
        "<a href="#cosmosdbgremlindatabasename" title="CosmosdbGremlinDatabaseName">CosmosdbGremlinDatabaseName</a>" : <i>String</i>,
        "<a href="#cosmosdbgremlingraphname" title="CosmosdbGremlinGraphName">CosmosdbGremlinGraphName</a>" : <i>String</i>,
        "<a href="#cosmosdbmongodatabasename" title="CosmosdbMongoDatabaseName">CosmosdbMongoDatabaseName</a>" : <i>String</i>,
        "<a href="#cosmosdbsqldatabasename" title="CosmosdbSqlDatabaseName">CosmosdbSqlDatabaseName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SpringCloudAppCosmosdbAssociation
Properties:
    <a href="#apitype" title="ApiType">ApiType</a>: <i>String</i>
    <a href="#cosmosdbaccesskey" title="CosmosdbAccessKey">CosmosdbAccessKey</a>: <i>String</i>
    <a href="#cosmosdbaccountid" title="CosmosdbAccountId">CosmosdbAccountId</a>: <i>String</i>
    <a href="#cosmosdbcassandrakeyspacename" title="CosmosdbCassandraKeyspaceName">CosmosdbCassandraKeyspaceName</a>: <i>String</i>
    <a href="#cosmosdbgremlindatabasename" title="CosmosdbGremlinDatabaseName">CosmosdbGremlinDatabaseName</a>: <i>String</i>
    <a href="#cosmosdbgremlingraphname" title="CosmosdbGremlinGraphName">CosmosdbGremlinGraphName</a>: <i>String</i>
    <a href="#cosmosdbmongodatabasename" title="CosmosdbMongoDatabaseName">CosmosdbMongoDatabaseName</a>: <i>String</i>
    <a href="#cosmosdbsqldatabasename" title="CosmosdbSqlDatabaseName">CosmosdbSqlDatabaseName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApiType

Specifies the api type which should be used when connecting to the CosmosDB Account. Possible values are `cassandra`, `gremlin`, `mongo`, `sql` or `table`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbAccessKey

Specifies the CosmosDB Account access key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbAccountId

Specifies the ID of the CosmosDB Account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbCassandraKeyspaceName

Specifies the name of the Cassandra Keyspace which the Spring Cloud App should be associated with. Should only be set when `api_type` is `cassandra`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbGremlinDatabaseName

Specifies the name of the Gremlin Database which the Spring Cloud App should be associated with. Should only be set when `api_type` is `gremlin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbGremlinGraphName

Specifies the name of the Gremlin Graph which the Spring Cloud App should be associated with. Should only be set when `api_type` is `gremlin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbMongoDatabaseName

Specifies the name of the Mongo Database which the Spring Cloud App should be associated with. Should only be set when `api_type` is `mongo`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbSqlDatabaseName

Specifies the name of the Sql Database which the Spring Cloud App should be associated with. Should only be set when `api_type` is `sql`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Spring Cloud Application Association. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpringCloudAppId

Specifies the ID of the Spring Cloud Application where this Association is created. Changing this forces a new resource to be created.

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

