# Terraform::AzureRM::ApiManagementBackend

Manages a backend within an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagementBackend",
    "Properties" : {
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentials.md">Credentials</a>, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>[ <a href="proxy.md">Proxy</a>, ... ]</i>,
        "<a href="#servicefabriccluster" title="ServiceFabricCluster">ServiceFabricCluster</a>" : <i>[ <a href="servicefabriccluster.md">ServiceFabricCluster</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="tls.md">Tls</a>, ... ]</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorization.md">Authorization</a>, ... ]</i>,
        "<a href="#serverx509name" title="ServerX509Name">ServerX509Name</a>" : <i>[ <a href="serverx509name.md">ServerX509Name</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagementBackend
Properties:
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentials.md">Credentials</a></i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>
      - <a href="proxy.md">Proxy</a></i>
    <a href="#servicefabriccluster" title="ServiceFabricCluster">ServiceFabricCluster</a>: <i>
      - <a href="servicefabriccluster.md">ServiceFabricCluster</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="tls.md">Tls</a></i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorization.md">Authorization</a></i>
    <a href="#serverx509name" title="ServerX509Name">ServerX509Name</a>: <i>
      - <a href="serverx509name.md">ServerX509Name</a></i>
</pre>

## Properties

#### ApiManagementName

The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the API Management backend. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol used by the backend host. Possible values are `http` or `soap`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The title of the backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of the backend host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentials.md">Credentials</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: List of <a href="proxy.md">Proxy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceFabricCluster

_Required_: No

_Type_: List of <a href="servicefabriccluster.md">ServiceFabricCluster</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of <a href="tls.md">Tls</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of <a href="authorization.md">Authorization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerX509Name

_Required_: No

_Type_: List of <a href="serverx509name.md">ServerX509Name</a>

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

