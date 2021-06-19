# TF::AzureRM::MediaStreamingPolicy

Manages a Streaming Policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MediaStreamingPolicy",
    "Properties" : {
        "<a href="#defaultcontentkeypolicyname" title="DefaultContentKeyPolicyName">DefaultContentKeyPolicyName</a>" : <i>String</i>,
        "<a href="#mediaservicesaccountname" title="MediaServicesAccountName">MediaServicesAccountName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#commonencryptioncbcs" title="CommonEncryptionCbcs">CommonEncryptionCbcs</a>" : <i>[ <a href="commonencryptioncbcsdefinition.md">CommonEncryptionCbcsDefinition</a>, ... ]</i>,
        "<a href="#commonencryptioncenc" title="CommonEncryptionCenc">CommonEncryptionCenc</a>" : <i>[ <a href="commonencryptioncencdefinition.md">CommonEncryptionCencDefinition</a>, ... ]</i>,
        "<a href="#noencryptionenabledprotocols" title="NoEncryptionEnabledProtocols">NoEncryptionEnabledProtocols</a>" : <i>[ <a href="noencryptionenabledprotocolsdefinition.md">NoEncryptionEnabledProtocolsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MediaStreamingPolicy
Properties:
    <a href="#defaultcontentkeypolicyname" title="DefaultContentKeyPolicyName">DefaultContentKeyPolicyName</a>: <i>String</i>
    <a href="#mediaservicesaccountname" title="MediaServicesAccountName">MediaServicesAccountName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#commonencryptioncbcs" title="CommonEncryptionCbcs">CommonEncryptionCbcs</a>: <i>
      - <a href="commonencryptioncbcsdefinition.md">CommonEncryptionCbcsDefinition</a></i>
    <a href="#commonencryptioncenc" title="CommonEncryptionCenc">CommonEncryptionCenc</a>: <i>
      - <a href="commonencryptioncencdefinition.md">CommonEncryptionCencDefinition</a></i>
    <a href="#noencryptionenabledprotocols" title="NoEncryptionEnabledProtocols">NoEncryptionEnabledProtocols</a>: <i>
      - <a href="noencryptionenabledprotocolsdefinition.md">NoEncryptionEnabledProtocolsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DefaultContentKeyPolicyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediaServicesAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonEncryptionCbcs

_Required_: No

_Type_: List of <a href="commonencryptioncbcsdefinition.md">CommonEncryptionCbcsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonEncryptionCenc

_Required_: No

_Type_: List of <a href="commonencryptioncencdefinition.md">CommonEncryptionCencDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoEncryptionEnabledProtocols

_Required_: No

_Type_: List of <a href="noencryptionenabledprotocolsdefinition.md">NoEncryptionEnabledProtocolsDefinition</a>

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

