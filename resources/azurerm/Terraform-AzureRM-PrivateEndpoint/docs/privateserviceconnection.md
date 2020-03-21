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

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateConnectionResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubresourceNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

