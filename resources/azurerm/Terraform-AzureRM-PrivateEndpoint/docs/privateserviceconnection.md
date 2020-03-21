# Terraform::AzureRM::PrivateEndpoint PrivateServiceConnection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ismanualconnection" title="IsManualConnection">IsManualConnection</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#privateconnectionresourceid" title="PrivateConnectionResourceId">PrivateConnectionResourceId</a>" : <i>String</i>,
    "<a href="#requestmessage" title="RequestMessage">RequestMessage</a>" : <i>String</i>,
    "<a href="#subresourcenames" title="SubresourceNames">SubresourceNames</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ismanualconnection" title="IsManualConnection">IsManualConnection</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#privateconnectionresourceid" title="PrivateConnectionResourceId">PrivateConnectionResourceId</a>: <i>String</i>
<a href="#requestmessage" title="RequestMessage">RequestMessage</a>: <i>String</i>
<a href="#subresourcenames" title="SubresourceNames">SubresourceNames</a>: <i>
      - String</i>
</pre>

## Properties

#### IsManualConnection

Does the Private Endpoint require Manual Approval from the remote resource owner? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the Name of the Private Service Connection. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateConnectionResourceId

The ID of the Private Link Enabled Remote Resource which this Private Endpoint should be connected to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMessage

A message passed to the owner of the remote resource when the private endpoint attempts to establish the connection to the remote resource. The request message can be a maximum of `140` characters in length. Only valid if `is_manual_connection` is set to `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubresourceNames

A list of subresource names which the Private Endpoint is able to connect to. `subresource_names` corresponds to `group_id`. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

