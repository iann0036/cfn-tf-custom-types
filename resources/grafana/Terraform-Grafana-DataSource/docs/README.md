# Terraform::Grafana::DataSource

The data source resource allows a data source to be created on a Grafana server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Grafana::DataSource",
    "Properties" : {
        "<a href="#accessmode" title="AccessMode">AccessMode</a>" : <i>String</i>,
        "<a href="#basicauthenabled" title="BasicAuthEnabled">BasicAuthEnabled</a>" : <i>Boolean</i>,
        "<a href="#basicauthpassword" title="BasicAuthPassword">BasicAuthPassword</a>" : <i>String</i>,
        "<a href="#basicauthusername" title="BasicAuthUsername">BasicAuthUsername</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#jsondata" title="JsonData">JsonData</a>" : <i>[ <a href="jsondata.md">JsonData</a>, ... ]</i>,
        "<a href="#securejsondata" title="SecureJsonData">SecureJsonData</a>" : <i>[ <a href="securejsondata.md">SecureJsonData</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Grafana::DataSource
Properties:
    <a href="#accessmode" title="AccessMode">AccessMode</a>: <i>String</i>
    <a href="#basicauthenabled" title="BasicAuthEnabled">BasicAuthEnabled</a>: <i>Boolean</i>
    <a href="#basicauthpassword" title="BasicAuthPassword">BasicAuthPassword</a>: <i>String</i>
    <a href="#basicauthusername" title="BasicAuthUsername">BasicAuthUsername</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#jsondata" title="JsonData">JsonData</a>: <i>
      - <a href="jsondata.md">JsonData</a></i>
    <a href="#securejsondata" title="SecureJsonData">SecureJsonData</a>: <i>
      - <a href="securejsondata.md">SecureJsonData</a></i>
</pre>

## Properties

#### AccessMode

The method by which the browser-based Grafana
application will access the data source. The default is "proxy", which means
that the application will make requests via a proxy endpoint on the Grafana
server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthEnabled

- If true, HTTP basic authentication will
be used to make requests.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthPassword

The
password to use for basic auth.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuthUsername

The
username to use for basic auth.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

The name of the
database to use on the selected data source server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

If true, the data source will be the default
source used by the Grafana server. Only one data source on a server can be
the default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the data source within the Grafana
server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password to use to
authenticate to the data source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The data source type. Must be one of the data source
keywords supported by the Grafana server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL for the data source. The type of URL required
varies depending on the chosen data source type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username to use to
authenticate to the data source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonData

_Required_: No

_Type_: List of <a href="jsondata.md">JsonData</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureJsonData

_Required_: No

_Type_: List of <a href="securejsondata.md">SecureJsonData</a>

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

