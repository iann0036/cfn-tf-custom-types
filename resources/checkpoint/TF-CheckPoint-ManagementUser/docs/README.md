# TF::CheckPoint::ManagementUser

This resource allows you to execute Check Point User.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementUser",
    "Properties" : {
        "<a href="#allowedlocations" title="AllowedLocations">AllowedLocations</a>" : <i>[ <a href="allowedlocationsdefinition.md">AllowedLocationsDefinition</a>, ... ]</i>,
        "<a href="#authenticationmethod" title="AuthenticationMethod">AuthenticationMethod</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#connectdaily" title="ConnectDaily">ConnectDaily</a>" : <i>Boolean</i>,
        "<a href="#connectondays" title="ConnectOnDays">ConnectOnDays</a>" : <i>[ String, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ <a href="encryptiondefinition.md">EncryptionDefinition</a>, ... ]</i>,
        "<a href="#expirationdate" title="ExpirationDate">ExpirationDate</a>" : <i>String</i>,
        "<a href="#fromhour" title="FromHour">FromHour</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>" : <i>String</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>String</i>,
        "<a href="#tacacsserver" title="TacacsServer">TacacsServer</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#tohour" title="ToHour">ToHour</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementUser
Properties:
    <a href="#allowedlocations" title="AllowedLocations">AllowedLocations</a>: <i>
      - <a href="allowedlocationsdefinition.md">AllowedLocationsDefinition</a></i>
    <a href="#authenticationmethod" title="AuthenticationMethod">AuthenticationMethod</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#connectdaily" title="ConnectDaily">ConnectDaily</a>: <i>Boolean</i>
    <a href="#connectondays" title="ConnectOnDays">ConnectOnDays</a>: <i>
      - String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - <a href="encryptiondefinition.md">EncryptionDefinition</a></i>
    <a href="#expirationdate" title="ExpirationDate">ExpirationDate</a>: <i>String</i>
    <a href="#fromhour" title="FromHour">FromHour</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>: <i>String</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>String</i>
    <a href="#tacacsserver" title="TacacsServer">TacacsServer</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#tohour" title="ToHour">ToHour</a>: <i>String</i>
</pre>

## Properties

#### AllowedLocations

User allowed locations. allowed_locations blocks are documented below.

_Required_: No

_Type_: List of <a href="allowedlocationsdefinition.md">AllowedLocationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationMethod

Authentication method.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectDaily

Connect every day.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectOnDays

Days users allow to connect.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

User email.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

User encryption. encryption blocks are documented below.

_Required_: No

_Type_: List of <a href="encryptiondefinition.md">EncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationDate

Expiration date in format: yyyy-MM-dd.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromHour

Allow users connect from hour.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Checkpoint password authentication method identified by the name or UID. Must be set when "authentication-method" was selected to be "Check Point Password".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneNumber

User phone number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

RADIUS server object identified by the name or UID. Must be set when "authentication-method" was selected to be "RADIUS".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TacacsServer

TACACS server object identified by the name or UID. Must be set when "authentication-method" was selected to be "TACACS".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

User template name or UID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToHour

Allow users connect until hour.

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

#### Id

Returns the <code>Id</code> value.

