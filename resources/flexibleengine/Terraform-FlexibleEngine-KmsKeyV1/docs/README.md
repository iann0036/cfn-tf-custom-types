# Terraform::FlexibleEngine::KmsKeyV1

Manages a V1 key resource within KMS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::KmsKeyV1",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#keyalias" title="KeyAlias">KeyAlias</a>" : <i>String</i>,
        "<a href="#keydescription" title="KeyDescription">KeyDescription</a>" : <i>String</i>,
        "<a href="#pendingdays" title="PendingDays">PendingDays</a>" : <i>String</i>,
        "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::KmsKeyV1
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#keyalias" title="KeyAlias">KeyAlias</a>: <i>String</i>
    <a href="#keydescription" title="KeyDescription">KeyDescription</a>: <i>String</i>
    <a href="#pendingdays" title="PendingDays">PendingDays</a>: <i>String</i>
    <a href="#realm" title="Realm">Realm</a>: <i>String</i>
</pre>

## Properties

#### IsEnabled

Specifies whether the key is enabled. Defaults to true.
Changing this updates the state of existing key.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlias

The alias in which to create the key. It is required when
we create a new key. Changing this updates the alias of key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyDescription

The description of the key as viewed in FlexibleEngine console.
Changing this updates the description of key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingDays

Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 1096 days. Defaults to 7.
It only be used when delete a key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

Region where a key resides. Changing this creates a new key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### DefaultKeyFlag

Returns the <code>DefaultKeyFlag</code> value.

#### DomainId

Returns the <code>DomainId</code> value.

#### ExpirationTime

Returns the <code>ExpirationTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Origin

Returns the <code>Origin</code> value.

#### ScheduledDeletionDate

Returns the <code>ScheduledDeletionDate</code> value.

